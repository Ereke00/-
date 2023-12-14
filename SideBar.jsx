import React, { useState } from 'react';
import styles from './SideBar.module.scss';

const Sidebar = ({ categories, handleCategoryClick }) => {
    const [showSidebar, setShowSidebar] = useState(false);

    const toggleSidebar = () => {
        setShowSidebar(!showSidebar);
    };

    return (
        <div className={styles.wrapper}>
            <div className={`${styles.sidebar} ${showSidebar ? styles.show_sidebar : null}`}>
                <div className={styles.indicator} onClick={toggleSidebar}>
                    Меню {showSidebar ? '←' : '→'}
                </div>
                <div className={styles.content}>
                    <div className={styles.menu}>
                        <h2>Меню</h2>
                        {categories.map((category, index) => (
                            <div
                                key={index}
                                className={styles.category}
                                onClick={() => handleCategoryClick(category)}
                            >
                                {category}
                            </div>
                        ))}
                    </div>
                </div>
            </div>
            <div className={styles.mainContent}>
                {/* Ваш основной контент */}
            </div>
        </div>
    );
};

export default Sidebar;
