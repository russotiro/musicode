import React from "react";
import styles from "../styles/button.module.css";
import { useNavigate } from "react-router-dom"
;
export interface buttonProps {
    text: string;
    onEditor: boolean
    //title: string;
}

const ActionButton = (props:buttonProps) => {
    //pass title in as part of button props 
    const path = props.onEditor ? "/" : "/editor";
    const navigate = useNavigate();
    const text = props.text;
    return (
        <button className={styles.navButton}
                onClick={() => navigate(path)}> {text} </button>
    );
} 


export default ActionButton