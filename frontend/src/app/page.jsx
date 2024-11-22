"use client";

import React, { useState, useEffect, useRef } from "react";
import "./styles.css"; // Import CSS file for styling
import "react-toastify/dist/ReactToastify.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faCheck,
  faStop,
  faUser,
  faVolumeHigh,
} from "@fortawesome/free-solid-svg-icons";
import { faCopy, faMoon, faSun } from "@fortawesome/free-regular-svg-icons";
import axios from "axios";

import { ThreeDots } from "react-loader-spinner";
import { ToastContainer, toast } from "react-toastify";
import DownArrowButton from "./DownArrowButton";
import Stars from "@/components/feedback/stars";
import UserNameModal from "../components/userNameModal/page";
import Image from "next/image";

const generateSessionId = () => {
  const timestamp = Date.now().toString();
  const randomString = Math.random().toString(36).substring(2, 15);
  return `${timestamp}-${randomString}`;
};

const App = () => {
  const url_machine = process.env.NEXT_PUBLIC_URL;

  const [sessionId, setSessionId] = useState("");
  const [inputText, setInputText] = useState("");
  const [chatData, setChatData] = useState([]);
  const [copiedReference, setCopiedReference] = useState(null);
  const [mainAnswerCopied, setMainAnswerCopied] = useState(false);
  const [loading, setLoading] = useState(false);
  const [utility, setUtility] = useState({
    toggleCopy: false,
    toggleReadAloud: false,
  });
  const [cancelTokenSource, setCancelTokenSource] = useState(null);
  const [theme, setTheme] = useState("dark");

  // for down arrow key
  const [showDownArrowButton, setShowDownArrowButton] = useState(false);
  const chatContainerRef = useRef(null);

  // for saving the data in a single db
  const [chatId, setChatId] = useState(null);
  const inputBoxRef = useRef(null);

  // handling email model popup for adding username
  const [showModal, setShowModal] = useState(false);
  const [userName, setUserName] = useState("");

  // state to handle selected model
  const [selectedModel, setSelectedModel] = useState("OpenAI");

  // check for stored userName address in session storage.
  useEffect(() => {
    const storedUserName = sessionStorage.getItem("userName");
    if (!storedUserName) {
      setShowModal(true);
    } else {
      setUserName(storedUserName);
    }
  }, []);

  // saving userNAme address
  const handleUserName = (name) => {
    setUserName(name.split("@")[0]);
  };

  useEffect(() => {
    const handleSessionRefresh = () => {
      const newSessionId = generateSessionId();
      localStorage.setItem("sessionId", newSessionId);
      setSessionId(newSessionId);
      setChatData([]); // Clear the chat data for the new session
    };
    const storedSessionId = localStorage.getItem("sessionId");
    if (storedSessionId) {
      setSessionId(storedSessionId);
    } else {
      handleSessionRefresh();
    }
    console.log("Session ID:", storedSessionId);
    window.addEventListener("beforeunload", handleSessionRefresh);
    const handleScroll = () => {
      const chatContainer = chatContainerRef.current;
      const scrollPosition =
        chatContainer.scrollHeight -
        chatContainer.scrollTop -
        chatContainer.clientHeight;

      if (scrollPosition > 1) {
        setShowDownArrowButton(true);
      } else {
        setShowDownArrowButton(false);
      }
    };

    const chatContainer = chatContainerRef.current;
    if (chatContainer) {
      chatContainer.addEventListener("scroll", handleScroll);
    }

    return () => {
      const chatContainer = chatContainerRef.current;
      if (chatContainer) {
        chatContainer.removeEventListener("scroll", handleScroll);
      }
    };
  }, []);

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
  };

  const handleQuestionClick = (chatIndex) => {
    const chatElement = document.querySelectorAll(".chat-data-container")[
      chatIndex
    ];
    chatElement.scrollIntoView({ behavior: "smooth" });
  };

  const newChatRef = useRef(null);

  useEffect(() => {
    if (mainAnswerCopied) {
      const timeoutId = setTimeout(() => {
        setMainAnswerCopied(false); // Reset the main answer copied state after the timeout
      }, 2500);

      return () => clearTimeout(timeoutId); // Cleanup the timeout if the component unmounts
    }
  }, [mainAnswerCopied]);

  useEffect(() => {
    if (utility.toggleCopy || copiedReference) {
      const timeoutId = setTimeout(() => {
        setUtility({ ...utility, toggleCopy: false });
        setCopiedReference(null); // Reset the copied reference after the timeout
      }, 2000);

      return () => clearTimeout(timeoutId); // Cleanup the timeout if the component unmounts
    }
  }, [utility.toggleCopy, copiedReference]);

  const handleIconClick = (option, chatAnswer = "") => {
    const speechSynthesis = window.speechSynthesis;
    switch (option) {
      case "Copy":
        navigator.clipboard.writeText(chatAnswer);
        setCopiedReference(chatAnswer);
        break;
      case "CopyMain":
        setUtility({ ...utility, toggleCopy: true });
        setMainAnswerCopied(true);
        navigator.clipboard.writeText(chatAnswer);
        break;
      case "Read":
        setUtility({ ...utility, toggleReadAloud: true });
        let text = new SpeechSynthesisUtterance(chatAnswer);
        speechSynthesis.speak(text);
        break;

      case "stopRead":
        setUtility({ ...utility, toggleReadAloud: false });
        speechSynthesis.cancel();
        break;

      default:
        break;
    }
  };



  const handleQuerySubmit = async (event) => {
    event.preventDefault();
    if (inputText.trim() !== "") {
      setLoading(true);
      const cancelToken = axios.CancelToken.source();
      setCancelTokenSource(cancelToken);
      try {
        let queryParams = {
          queryText: inputText,
          name: userName,
          modelName: selectedModel,
          sessionId: sessionId
        };
        console.log(queryParams);
        let url = `http://${url_machine}/generate_answer`;

        const response = await axios.post(url, null, {
          params: queryParams,
          cancelToken: cancelToken.token,
          headers: {
            "Content-Type": "application/json",
            "Session-Id": sessionId,
          },
        });

        setChatData([...chatData, response.data]);
        console.log("hello this after posting the question", response.data);
        setChatId(response.data._id); // Set chatId here

        setInputText("");
        setUtility({ toggleCopy: false, toggleReadAloud: false });

        // Scroll to the new chat after adding it
        setTimeout(() => {
          if (newChatRef.current) {
            newChatRef.current.scrollIntoView({ behavior: "smooth" });
          }
        }, 100);
      } catch (error) {
        if (axios.isCancel(error)) {
          console.log("Request canceled:", error.message);
        } else {
          console.log("Error:", error);
        }
      }
      setLoading(false);
    }
  };


  const handleCancelGenerateApiCall = () => {
    // If there's an ongoing request, cancel it
    if (cancelTokenSource) {
      cancelTokenSource.cancel("Request canceled by user.");
    }
  };

  return (
    <>
      <div className="container">
        <ToastContainer
          position="top-right"
          autoClose={3000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme={theme}
        />
        <div className="sidebar">
          <div className="dropdown-container">
            <label>Select Model</label>
            <select
              className="project-dropdown"
              onChange={(event) => setSelectedModel(event.target.value)}
              value={selectedModel}
            >
              <option value="OpenAI">OpenAI</option>
            </select>
          </div>

          <h4>Recent Questions</h4>

          <div className="history-sidebar">
            {chatData.map((chat, chatIndex) => (
              <div
                key={chatIndex}
                className="history-item"
                onClick={() => handleQuestionClick(chatIndex)}
              >
                {chat.user_question}
              </div>
            ))}
          </div>
        </div>
        {loading && (
          <div className="loader generating-answer-wrapper">
            <div className="generating-answer-text-container">
              <div>Generating Answer </div>
              <ThreeDots
                visible={true}
                height="60"
                width="60"
                color="skyblue"
                radius="9"
                ariaLabel="three-dots-loading"
                wrapperStyle={{}}
                wrapperClass=""
              />
            </div>
            <div
              className="abort-generation"
              onClick={handleCancelGenerateApiCall}
            >
              <FontAwesomeIcon className="stop-icon" icon={faStop} />
              <span style={{ cursor: "pointer" }}>Stop generating</span>
            </div>
          </div>
        )}
        <div className="main-container">
          <div className="navigator">
            <div className="logo_container">
              <Image
                src={
                  theme == "light"
                    ? "/images/shopwise-black-text.png"
                    : "/images/shopwise-white-text-transparent-background.png"
                }
                alt="valtech logo"
                width={180}
                height={40}
              />
            </div>
            <div className="profile_section">
              <div>
                <p>{userName ? "Hi " + userName : "Guest User"}</p>
              </div>
              <div className="button-container">
                <label className="switch">
                  <input type="checkbox" onChange={toggleTheme} />
                  <span className="slider"></span>

                  <FontAwesomeIcon
                    id="sun-icon"
                    icon={faSun}
                    style={{
                      color: theme == "dark" ? "#000" : "#fff",
                    }}
                  />
                  <FontAwesomeIcon
                    id="moon-icon"
                    icon={faMoon}
                    style={{
                      color: theme == "light" ? "#000" : "#fff",
                    }}
                  />
                </label>
              </div>
            </div>
          </div>

          <div className="chat-container" ref={chatContainerRef}>
            {chatData.length > 0 ? (
              chatData.map((chat, chatIndex) => (
                <div
                  className="chat-data-container"
                  key={chatIndex}
                  ref={chatIndex === chatData.length - 1 ? newChatRef : null}
                >
                  <div className="chat-data" key={chatIndex}>
                    <div className="question-wrapper">
                      <div className="chat-icon-container">
                        <FontAwesomeIcon
                          className="chat-icon"
                          icon={faUser}
                          style={{ color: "var(--icon-color)" }}
                        />
                      </div>
                      <div className="question-prompt">
                        {chat?.user_question}
                      </div>
                    </div>

                    {/* formatting the code */}
                    <div className="chat-logo-wrapper">
                      <span className="answer-logo">*</span>
                      <span className="chat-icon-text"> Answer: </span>
                    </div>

                    <div className="question-answer-text">
                      <div style={{ paddingLeft: "20px" }}>
                        {chat?.main_answer && (
                          <>
                            {chat.main_answer
                              .split(/(?<=\.)\s+(?=\d+\.)/) // Updated regex to check for a space after the period
                              .map((paragraph, index) => {
                                const lines = paragraph
                                  .split(/\n/)
                                  .map((line) => line.trim())
                                  .filter((line) => line);

                                return lines.map((line, lineIndex) => {
                                  const bulletMatch = line.match(/^(\d+\.)\s*(.*)/);

                                  const formattedText = line.replace(
                                    /\*\*(.+?)\*\*/g,
                                    "<strong>$1</strong>"
                                  );

                                  return (
                                    <p
                                      key={`${index}-${lineIndex}`}
                                      style={{
                                        marginTop: "10px",
                                        marginBottom: "10px",
                                        marginLeft: "20px",
                                      }}
                                    >
                                      <span
                                        dangerouslySetInnerHTML={{
                                          __html: formattedText,
                                        }}
                                      />
                                    </p>
                                  );
                                });
                              })}
                          </>
                        )}
                      </div>
                    </div>

                    <div className="chat-utility-icons-container">
                      <Stars
                        chat={chat}
                        url={url_machine}
                      />
                      {utility.toggleCopy ? (
                        <div className="utility-icons" title="Copied">
                          <FontAwesomeIcon
                            icon={faCheck}
                            style={{ color: "var(--icon-color)" }}
                          />
                        </div>
                      ) : (
                        <div
                          className="utility-icons"
                          onClick={() =>
                            handleIconClick("CopyMain", chat?.main_answer)
                          }
                          title="Copy"
                        >
                          <FontAwesomeIcon
                            icon={faCopy}
                            style={{ color: "var(--icon-color)" }}
                          />
                        </div>
                      )}
                      {utility.toggleReadAloud ? (
                        <div
                          className="utility-icons"
                          onClick={() => handleIconClick("stopRead", "")}
                          title="Stop reading"
                        >
                          <FontAwesomeIcon
                            icon={faStop}
                            style={{ color: "var(--icon-color)" }}
                          />
                        </div>
                      ) : (
                        <div
                          className="utility-icons"
                          onClick={() =>
                            handleIconClick("Read", chat?.main_answer)
                          }
                          title="Read aloud"
                        >
                          <FontAwesomeIcon
                            icon={faVolumeHigh}
                            style={{ color: "var(--icon-color)" }}
                          />
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <div className="initial-label">
                <div>How can I help you today?</div>
              </div>
            )}
          </div>

          {showDownArrowButton && (
            <DownArrowButton
              onClick={() => {
                const chatContainer = chatContainerRef.current;
                chatContainer.scrollTo({
                  top: chatContainer.scrollHeight,
                  behavior: "smooth",
                });
                if (inputBoxRef.current) {
                  inputBoxRef.current.focus();
                }
              }}
            />
          )}
          <div className="bottom-container">
            <form onSubmit={handleQuerySubmit}>
              <input
                type="text"
                value={inputText}
                className="input-box"
                placeholder={`Please enter your question here`}
                onChange={(event) => setInputText(event.target.value)}
                ref={inputBoxRef}
              />
            </form>
            <div className="disclaimer-text">
              Disclaimer: This is an AI generated content. Please double-check responses.
            </div>
          </div>
        </div>
      </div>

      {showModal && (
        <UserNameModal
          onClose={() => setShowModal(false)}
          onUserNameSave={handleUserName}
        />
      )}
    </>
  );
};

export default App;
