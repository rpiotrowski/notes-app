import React, {useState, useEffect} from 'react'
import { useParams } from "react-router-dom";

const NotePage = () => {

    let params = useParams();
    let noteId = params.id
    let [note,setNote] = useState(null)

    useEffect(() => {
        getNote()
    }, [noteId])

    let getNote = async () => {
        let response = await fetch(`/api/notes/${noteId}`)
        let data = await response.json()
        setNote(data)
    }

    return (
        <div>
            <p>Single Note {note?.body}</p>
        </div>
    )
}

export default NotePage