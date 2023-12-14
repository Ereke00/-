// MessagesList.js
import React from 'react';
import styles from "./MessagesList.module.scss"
const MessagesList = (props) => {
    const { messages, currentCategory } = props
    let category = currentCategory
    if (category === "0") {
        category = "Спам"
    }

    console.log("mess", messages)
    return (
        <div className={styles.messages_list}>
            <h1>
                {category}
            </h1>
            <div>
                {messages && messages.map((message, index) => (
                    <div className={styles.mess_wrap} key={index}>
                        <p><strong>От:</strong> {message.sender}</p>
                        <p><strong>Кому:</strong> {message.recipient}</p>
                        <p><strong>Текст:</strong> {message.text}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};
export default MessagesList