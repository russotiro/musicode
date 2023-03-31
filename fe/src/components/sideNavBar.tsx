import React from "react";
import { NavLink } from "react-router-dom";

import ActionButton, { buttonProps } from "./actionButton";

import styles from "../styles/navBar.module.css";

interface navBarProps {
    isOnEditor: boolean
}

interface navLinkProps {
	slug: string; 
	text: string;
}


// TODO make wrapper for navlink

const NavBar = (props: navBarProps) => {
	const newProjButton: buttonProps  = {
		text: "New Project",
		onEditor: props.isOnEditor
	}

	const backButton : buttonProps = {
		text: "Back to Files",
		onEditor:true
	}



	if (props.isOnEditor) {
		return (
			<nav className={styles.navBar}>
				<ActionButton text={newProjButton.text}
							  onEditor={newProjButton.onEditor}/>
				<ActionButton text={backButton.text}
							  onEditor={backButton.onEditor}/>
			</nav>
		); 
	} else {
		return (
				<nav className={styles.navBar}>
					<ActionButton text={newProjButton.text}
								  onEditor={newProjButton.onEditor}/>
					<NavLink 
							className={({isActive}) => 
										isActive ? styles.navactive	
												: styles.nav }
							to="/"> Projects </NavLink>
					<NavLink 
							className={({isActive}) => 
										isActive ? styles.navactive	
												: styles.nav } 
							to="/recently-deleted"> 
							Recently Deleted
					</NavLink>
				</nav>
			);
	}
};


// const StyledNavLink = (props: navLinkProps) => {
// 	const activeStyle = styles.navactive 
// 	const regStyle = styles.nav 
	
// 	const slug = props.slug
// 	const text = props.text

// 	return (
// 		<NavLink 
// 			className={({isActive}) => 
// 					isActive ? activeStyle 
// 				 			 : regStyle }
// 			to={slug} >
// 				{text}
// 			</NavLink>
// 	)
// }



export default NavBar