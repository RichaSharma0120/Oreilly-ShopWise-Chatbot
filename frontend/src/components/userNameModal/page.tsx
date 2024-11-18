"use client";
import React, { useEffect, useState } from 'react';
import styles from "./usernameModal.module.css";

const UserNameModal = ({ onClose, onUserNameSave }) => {
  const [userName, setUserName] = useState('');

  useEffect(() => {
    const storedUserName = sessionStorage.getItem('userName');
    if (storedUserName) {
      setUserName(storedUserName);
    }
  }, []);

  const handleSaveEmail = () => {

    if (userName) {
      sessionStorage.setItem('userName', userName);
      onUserNameSave(userName);
      onClose();
  };
}

  const handleClear = () => {
    setUserName('');
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    handleSaveEmail();
  };

  return (
    <div className={styles.modalBackground}>
      <div className={styles.modalContent}>
        <h2 className={styles.modalHeading}>Enter your name</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            className={`${styles.inputField} `}
            placeholder="Enter name"
          />
          <div className={styles.buttonContainer}>
            <button
              type="button"
              onClick={handleClear}
              className={styles.buttonClear}
            >
              Clear
            </button>
            <button
              type="submit"
              className={styles.button}
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default UserNameModal;
