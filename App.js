import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Sidebar from './SideBar';
import MessagesList from './MessageList';
import './App.css'
import styles from "./App.module.scss"
const App = () => {
  const [message, setMessage] = useState('');
  const [recipientValue, setRecipientValue] = useState('');
  const [senderValue, setSenderValue] = useState('');
  const [prediction, setPrediction] = useState('');
  const [sentMessages, setSentMessages] = useState(() => {
    const storedMessages = localStorage.getItem('sentMessages');
    return storedMessages ? JSON.parse(storedMessages) : [];
  });
  const [showForm, setShowForm] = useState(false);
  const [messagesByCategory, setMessagesByCategory] = useState({});
  const categories = ['Входящие', 'Спам', 'Проекты', 'Вакансии']; // ваш список категорий
  const [currentCategory, setCurrentCategory] = useState('Входящие');


  const handleCategoryClick = async (category) => {
    try {
      let categoryValue = category;

      if (category === 'Спам') {
        categoryValue = '0';
      }
      if (category === 'Вакансии') {
        categoryValue = "1";
      }
      if (category === 'Проекты') {
        categoryValue = "2";
      }
      console.log("categoryyy", categoryValue);
      const response = await axios.get(`http://127.0.0.1:5888/get_messages_by_category/${categoryValue}`);
      const messages = response.data.messages;


      if (category === 'Входящие') {
        setMessagesByCategory(messages);
      } else {
        setMessagesByCategory({ ...messagesByCategory, [categoryValue]: messages });
      }
      setMessagesByCategory(prevMessages => {
        return { ...prevMessages, [categoryValue]: messages };
      });
      console.log("messages,", messagesByCategory)
      setCurrentCategory(categoryValue);
      console.log(response);
      console.log(categoryValue);
      console.log(message);
    } catch (error) {
      console.error('Error fetching messages by category:', error);
    }
  };




  const handleSubmit = async () => {
    try {
      const responsePrediction = await axios.post('http://127.0.0.1:5888/predict_category', {
        message: message
      });
      const predictedCategory = responsePrediction.data.category;

      const responseSave = await axios.post('http://127.0.0.1:5888/save_message', {
        recipient: recipientValue,
        sender: senderValue,
        text: message,
        category: predictedCategory
      });

      if (responseSave.status === 200) {
        setPrediction(predictedCategory);
        const newMessage = {
          recipient: recipientValue,
          sender: senderValue,
          text: message,
          category: predictedCategory
        };
        const updatedMessages = [...sentMessages, newMessage];
        setSentMessages(updatedMessages);
        localStorage.setItem('sentMessages', JSON.stringify(updatedMessages));
        console.log("SERVER WORKING")
      } else {
        console.log("SERVER NOT WORKING")
      }

    } catch (error) {
      console.error('Error:', error);
    }
  }

  useEffect(() => {
    console.log('sentMessages:', sentMessages);
  }, [sentMessages]);

  useEffect(() => {
    const fetchMessagesByCategory = async () => {
      try {
        const categories = ['inbox', 'spam', 'projects', 'vacancies']; // Ваши категории
        const messages = {};

        for (const category of categories) {
          const response = await axios.get(`http://127.0.0.1:5888/get_messages_by_category/${category}`);
          messages[category] = response.data.messages;
        }
        setCurrentCategory('Входящие'); // Установка начальной категории по умолчанию

        setMessagesByCategory(messages);
      } catch (error) {
        console.error('Error fetching messages by category:', error);
      }
    };

    fetchMessagesByCategory();
  }, []);
  return (

    <div className="email-form">
      <Sidebar categories={categories} handleCategoryClick={handleCategoryClick} />
      <div className="main-content">
        {/* Отображение сообщений внутри выбранной категории */}
        <MessagesList messages={messagesByCategory[currentCategory]} currentCategory={currentCategory} />
      </div>
      {!showForm ? (
        <button className={styles.send_button} onClick={() => setShowForm(true)}>Отправить сообщение</button>
      ) : (
        <form className="email-form-fields">
          <label>От кого:</label>
          <input
            type="text"
            value={senderValue}
            onChange={(e) => setSenderValue(e.target.value)}
          />
          <label>Кому:</label>
          <input
            type="text"
            value={recipientValue}
            onChange={(e) => setRecipientValue(e.target.value)}
          />
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Введите ваше сообщение"
            rows={4}
            cols={50}
          />
          <button onClick={handleSubmit}>Отправить</button>
        </form>
      )}
      {prediction && <p>Предсказанная категория: {prediction}</p>}
      {/* {sentMessages.length > 0 && (
        <div className="sent-messages">
          <h2>Отправленные сообщения</h2>
          {sentMessages.map((msg, index) => (
            <div key={index} className="message">
              <p><strong>От:</strong> {msg.sender}</p>
              <p><strong>Кому:</strong> {msg.recipient}</p>
              <p><strong>Текст:</strong> {msg.text}</p>
            </div>
          ))}
        </div>
      )} */}

    </div>
  );
};

export default App;
