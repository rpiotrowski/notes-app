import React from 'react'
import { useParams } from "react-router-dom";

const NotePage = ({match}) => {

    let params = useParams();
    let noteId = params.id


    return (
        <div>
            <h1>Single Note {noteId}</h1>
        </div>
    )
}

export default NotePage