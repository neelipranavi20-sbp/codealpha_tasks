async function translateText() {

    const text = document.getElementById("inputText").value;
    const sourceLang = document.getElementById("sourceLang").value;
    const targetLang = document.getElementById("targetLang").value;

    const url = `https://api.mymemory.translated.net/get?q=${text}&langpair=${sourceLang}|${targetLang}`;

    try {

        const response = await fetch(url);
        const data = await response.json();

        document.getElementById("outputText").value =
            data.responseData.translatedText;

    } catch (error) {
        alert("Translation Failed");
        console.log(error);
    }
}

function copyText() {

    const output = document.getElementById("outputText");

    output.select();
    document.execCommand("copy");

    alert("Copied Successfully!");
}

function speakText() {

    const text = document.getElementById("outputText").value;

    const speech = new SpeechSynthesisUtterance(text);

    speech.lang = document.getElementById("targetLang").value;

    window.speechSynthesis.speak(speech);
}