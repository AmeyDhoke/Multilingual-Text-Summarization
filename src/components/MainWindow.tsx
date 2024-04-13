import React, {useState} from "react";
import api from "../api";

const MainWindow = () => {
    const [text, setText] = useState('');
    const [summarizedText, setSummary] = useState('');

    const summarizeText = async(text: any) => {
        const response = await api.get('/text/summarize', text);
        setSummary(response.data)
    }

    

    const handleOnChange = (event: any) => {
        setText(event.target.value);
    }

    return (
        <div className="h-screen flex gap-4 justify-evenly items-center bg-cyan-100">
            <div className="w-2/5 px-6 py-5  border-2 border-solid border-black h-96 rounded-lg bg-teal-300">
                <textarea
                    className="max-h-80 w-full p-4 rounded resize-none my-5 border-solid border-blue-600"
                    placeholder="Paste your text here..." onChange={handleOnChange}
                ></textarea>
                <button className={`bg-slate-200 w-auto ${text == ''? 'cursor-not-allowed' : '' }`} onClick={summarizeText} >Summarize</button>
            </div>
            <div className="bg-pink-500 border-2 border-solid w-2/5 border-black h-52 flex gap-2 items-center flex-shrink-0">
                <h1>This is the output of summarization</h1>
                <textarea className="max-h-80 w-full p-4 rounded resize-none my-5 border-solid border-blue-600" value={summarizedText}></textarea>
            </div>
        </div>
    );
};

export default MainWindow;
