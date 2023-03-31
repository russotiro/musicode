import React from "react";
import { useParams } from "react-router-dom";

import NavBar from "../components/sideNavBar";

import styles from "../styles/home.module.css";

// if this is a page we have to pass the info in 
// as a param along with the route  
const Editor = () => {
    const { title } = useParams();
    console.log(title);

    return (
        <div className={styles.home}>
            <NavBar isOnEditor={true}/>
            <div>
                <h2> EDITOR </h2> 
                <a> {title} </a>
            </div>
        </div>
    );
}

export default Editor;