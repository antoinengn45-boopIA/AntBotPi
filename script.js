document.getElementById('trainBtn').addEventListener('click', () => {
    const val = document.getElementById('dataInput').value;
    const output = document.getElementById('output');
    
    if(val) {
        // Logique simplifiée de l'IA
        const result = val * 2; 
        output.innerText = "AntBotPi a analysé : " + result;
    } else {
        output.innerText = "Veuillez entrer une donnée valide.";
    }
});
