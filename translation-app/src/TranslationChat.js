import { useState, useEffect, useRef } from "react";
import "./TranslationChat.css"; // CSS 파일 import

const TranslationChat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // 채팅창 자동 스크롤
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // 메시지 전송 처리
  const handleSend = async () => {
    if (input.trim() === "") return;

    // 사용자 메시지 추가
    const userMessage = {
      id: Date.now(),
      text: input,
      isUser: true,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      // Flask 백엔드로 메시지 전송 및 번역 요청
      const response = await fetch("http://localhost:5000/datapost", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(input),
      });

      const data = await response.json();

      // 번역된 응답 메시지 추가
      const botMessage = {
        id: Date.now() + 1,
        text: data.result,
        isUser: false,
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error("번역 오류:", error);

      // 오류 메시지 추가
      const errorMessage = {
        id: Date.now() + 1,
        text: "번역 과정에서 오류가 발생했습니다. 다시 시도해주세요.",
        isUser: false,
        isError: true,
      };

      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  // 엔터 키 처리
  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-container">
      {/* 상단 헤더 */}
      <div className="chat-header">
        <h1>번역 채팅</h1>
      </div>

      {/* 채팅 메시지 영역 */}
      <div className="messages-container">
        <div className="messages-wrapper">
          {messages.length === 0 ? (
            <div className="empty-message">
              <p>메시지를 입력하면 번역해드립니다.</p>
            </div>
          ) : (
            messages.map((message) => (
              <div
                key={message.id}
                className={`message ${
                  message.isUser ? "user-message" : "bot-message"
                } ${message.isError ? "error-message" : ""}`}
              >
                <div className="message-bubble">{message.text}</div>
              </div>
            ))
          )}
          {loading && (
            <div className="message bot-message">
              <div className="message-bubble loading-bubble">
                <div className="loading-dots">
                  <div className="dot"></div>
                  <div className="dot"></div>
                  <div className="dot"></div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* 입력 영역 */}
      <div className="input-container">
        <div className="input-wrapper">
          <textarea
            className="message-input"
            placeholder="번역할 메세지를 입력하시오..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            rows="1"
          />
          <button
            className="send-button"
            onClick={handleSend}
            disabled={loading || input.trim() === ""}
          >
            전송
          </button>
        </div>
      </div>
    </div>
  );
};

export default TranslationChat;
