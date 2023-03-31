import React from "react";
import styles from "../styles/projects.module.css";
import IconButton from "./iconButton";
/**
 * List of projects on the home page. 
 * Takes in an array of ProjectProps 
 * Displays each of them as an entry 
 * 
 * returns the list of projects the user currently has
 */

/*
 * Props to Projects component 
 * contains the name of the project
 * and the date last modified  
 */
export interface ProjectProp {
    name: string,
    dateLastModified: string,
}

interface ProjectList {
    projects: ProjectProp[];
    isOnHome: boolean;
}

const Projects = (props: ProjectList) => {    
    let dateHeader = props.isOnHome ? "Date Last Modified" : "Date Deleted"
    const entries = props.projects.map(proj => (makeEntry(proj)));
    return(
        <>
            <div className={styles.header}>
                <div className={styles.projecttitle}> Project Name </div>
                <div className={styles.projectdate}> {dateHeader} </div>
                <div className={styles.actions}> Actions </div>
            </div>
            <div className={styles.projs}>
                {entries}
             </div>
        </>

    );
}

const makeEntry = (proj: ProjectProp) => {
    return (
        <ProjectEntry name={proj.name} dateLastModified={proj.dateLastModified} />
    );
}

const ProjectEntry = (project: ProjectProp) => {
    return (
        <div className={styles.project}>
            <div className={styles.projecttitle}> {project.name} </div>
            <div className={styles.projectdate}> {project.dateLastModified} </div>
            <div className={styles.actions}>
                <IconButton/><IconButton/> 
            </div>
        </div>
    );
}


export default Projects