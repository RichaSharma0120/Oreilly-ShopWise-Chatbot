"use client";

import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleDown } from '@fortawesome/free-solid-svg-icons';

const DownArrowButton = ({ onClick }) => {
  return (
    <div className="down-arrow-button" onClick={onClick}>
      <FontAwesomeIcon icon={faAngleDown}/>
    </div>
  );
};

export default DownArrowButton;