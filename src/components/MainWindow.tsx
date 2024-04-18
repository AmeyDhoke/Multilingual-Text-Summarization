import {useState} from "react";
import api from "../api";

const MainWindow = () => {
    const [text, setText] = useState('');
    const [summarizedText, setSummary] = useState('');
    const [language, setLanguage] = useState('');

    // const summarizeText = async(text: any) => {
    //     const response = await api.get('/text/summarize', text);
    //     setSummary(response.data)
    // }

    const summarizeMultiText = async(text: any, language?: any) => {
        const newtext = text.replace(/"/g,"'");
        console.log(newtext)
        console.log(language)
        const text_to_summarize = {
            text: newtext,
            lang: language
        }
        console.log(text_to_summarize.text);
        console.log(text_to_summarize.lang)
        const response = await api.post('/text/summarize2', text_to_summarize);
        setSummary(response.data)
    }

    const handleSelect = (event: any) => {
        setLanguage(event.target.value);
    }
    

    const handleOnChange = (event: any) => {
        setText(event.target.value);
        console.log(text)
    }

    const lang_options = [
        {label: "English", value: "english"},
        {label: "Hindi", value: "hindi"},
        {label: "Marathi", value: "marathi"},
    ]


    return (
        <div className="h-screen flex gap-4 justify-evenly items-center bg-cyan-100">
            <div className="w-2/5 px-6 py-5  border-2 border-solid border-black h-96 rounded-lg bg-teal-300">
                <textarea
                    className="h-1/2 w-full p-4 rounded resize-none my-5 border-solid border-blue-600"
                    placeholder="Paste your text here..." onChange={handleOnChange}
                ></textarea>
                <div>
                <p>Select output language</p>
                <select onChange={handleSelect}>
                    {lang_options.map(option =>(
                    <option value = {option.value}>{option.label}</option>
                    ))}
                </select>
                </div>
                <button className={`bg-slate-200 w-auto ${text == ''? 'cursor-not-allowed' : '' } mt-5`} onClick={() => summarizeMultiText(text, language)} >Summarize</button>
            </div>
            <div className="bg-pink-500 px-6 py-5 border-2 border-solid w-2/5 border-black h-96 rounded-lg flex flex-col gap-2 items-center flex-shrink-0">
                <h1>This is the output of summarization</h1>
                <textarea className="h-full w-full p-4 rounded resize-none my-5 border-solid border-blue-600 bg-white" disabled value={summarizedText}></textarea>

            </div>
        </div>
    );
};

export default MainWindow;
