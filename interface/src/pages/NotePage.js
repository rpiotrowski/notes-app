import React, {useState, useEffect} from 'react'
import {useParams, useNavigate, Link} from "react-router-dom";
import {ReactComponent as ArrowLeft} from '../assets/arrow-left.svg'

const NotePage = () => {

    let params = useParams()
    let navigate = useNavigate()
    let noteId = params.id
    let [note, setNote] = useState(null)

    useEffect(() => {
        getNote()
    }, [noteId])

    let getNote = async () => {
        if (noteId === 'new') return
        let response = await fetch(`/api/notes/${noteId}`)
        let data = await response.json()
        setNote(data)
    }

    let updateNote = async () => {
        await fetch(`/api/notes/${noteId}/update`, {
            method: "PUT",
            headers: {'Content-Type': "application/json"},
            body: JSON.stringify(note)
        })
    }


    let deleteNote = async () => {
        await fetch(`/api/notes/${noteId}/delete`, {
            method: "DELETE",
            headers: {'Content-Type': "application/json"},
            body: JSON.stringify(note)
        })
        navigate('/')
    }

    let handleSubmit = () => {
        updateNote()
        navigate('/')
    }

    return (
        <div className="note">
            <div className="note-header">
                <h3>
                    <ArrowLeft onClick={handleSubmit}/>
                </h3>
                {noteId !== 'new' ? (
                    <button onClick={deleteNote}>Delete</button>
                ) : (
                    <button onClick={handleSubmit}>Done</button>
                )}
            </div>
            <textarea onChange={(e) => {
                setNote({...note, 'body': e.target.value})
            }} defaultValue={note?.body}></textarea>
        </div>
    )
}

export default NotePage