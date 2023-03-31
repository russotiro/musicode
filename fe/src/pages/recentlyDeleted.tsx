import React, { useState } from "react";
import Projects from "../components/projects";
import NavBar from "../components/sideNavBar";
import styles from "../styles/home.module.css"

// import { ProjectProp } from "../components/projects";

type ProjectProp = {
    name: string,
    dateLastModified: string,
}

type ProjectList = ProjectProp[];


const RecentlyDeleted = () => {
    const proj1 : ProjectProp = { name: "deleteed", dateLastModified: "4.6.23" }
    const proj2 : ProjectProp = { name: "dfhdhd", dateLastModified: "4.4.23" }
    const proj3 : ProjectProp = { name: "ghfjghjrkjghkjehr", dateLastModified: "2.4.23" }

    const projs = [proj1, proj2, proj3]

    return (
        <div className={styles.home}>
            <NavBar isOnEditor={false}/>
            <Projects projects={projs} isOnHome={false}/>
        </div>
    );


}

export default RecentlyDeleted;