"use client";

import "../../app/styles.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faClose, fas } from "@fortawesome/free-solid-svg-icons";
import { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";


export default function FeedbackModal({
  setShowFeedBackModal,
  userRating,
  setUserRating,
  chat,
  url
}) {
  // State variables
  const [feedback, setFeedback] = useState("");
  const [rating, setRating] = useState(userRating);

  // console.log(chat)

  const closeFeedBackModal = () => {
    setShowFeedBackModal(false);
  };

  const handleFeedBackSubmit = async (event) => {
    event.preventDefault();
    setUserRating(rating);
    const feedback_obj = {
      feedback: feedback,
      question: chat.user_question,
      stars_given: rating
    };

    console.log("feedbak insde modal", feedback_obj);
    setShowFeedBackModal(false);

    axios
      .put(
        `http://${url}/submit_feedback?_id=${chat._id}`,
        feedback_obj
      )
      .then((response) => {
        console.log("res ===>", response.data);

        if (response.data.message == "Feedback submitted successfully") {
          toast.success(response.data.message, {
            position: "top-center",
            autoClose: 3000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
          });
        } else {
          toast.error("Something went wrong!!", {
            position: "top-center",
            autoClose: 3000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
          });
        }
      })

      .catch((err) => {
        console.log("err ===>", err);
        toast.error("Failed to submit feedback. Please try again.", {
          position: "top-center",
          autoClose: 3000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
        });
      });
  };

  return (
    <>
      <div className="feedback-modal-container">
        <div className="feedback-modal">
          <div className="close-feedback" onClick={closeFeedBackModal}>
            <FontAwesomeIcon icon={faClose} />
          </div>
          <div className="feedback-rating-container">
            {[1, 2, 3, 4, 5].map((starValue) => (
              <span
                key={starValue}
                onClick={() => setRating(starValue)}
                style={{
                  marginRight: "3px",
                  cursor: "pointer",
                  color: starValue <= rating ? "gold" : "grey",
                }}
              >
                ★
              </span>
            ))}
          </div>
          <div className="feedback-heading">
            <h2>Submit Feedback</h2>
          </div>
          <div>
            <div className="feedback-input-label">What's your feedback?</div>
            <textarea
              rows="5"
              value={feedback}
              className="feedback-input-box"
              placeholder="Please give your feedback"
              onChange={(event) => setFeedback(event.target.value)}
            />
          </div>
          <div className="feedback-button-container">
            <button
              className="feedback-button"
              type="submit"
              onClick={handleFeedBackSubmit}
            >
              Submit
            </button>
            <button
              className="feedback-button"
              type="button"
              onClick={closeFeedBackModal}
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
