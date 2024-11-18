"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import { toast } from "react-toastify";


export default function Stars({ chat,  url }) {
  const [currentRating, setCurrentRating] = useState(chat.rating); // Initialize with prop


  const handleStarClick = (starValue) => {
    setCurrentRating(starValue);
    const feedback_obj = {
      question: chat.user_question,
      stars_given: starValue
    };

    axios
      .put(`http://${url}/submit_feedback?_id=${chat._id}`, feedback_obj)
      .then((response) => {

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

  // Re-run when the chat prop changes
  useEffect(() => {
    setCurrentRating(chat.rating);
  }, [chat.rating]);

  return (
    <>
        <div className="utility-icons">
          {[1, 2, 3, 4, 5].map((star, index) => {
            const starValue = index + 1;
            return (
              <span
                key={starValue}
                onClick={() => handleStarClick(starValue)}
                style={{
                  marginRight: "3px",
                  cursor: "pointer",
                  color: starValue <= currentRating ? "gold" : "grey",
                }}
              >
                ★
              </span>
            );
          })}
        </div>
    </>
  );
}
