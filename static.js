const inputElements = document.querySelectorAll(".input");
const resultElement = document.querySelector("#result");

// add an event listener to the submit button
const submitButton = document.querySelector("#submit-button");
submitButton.addEventListener("click", () => {

  // get the user input values from the input elements
  const inputValues = Array.from(inputElements).map(element => parseInt(element.value));

  // send an HTTP POST request to the server with the input values
  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({inputs: inputValues})
  })
  .then(response => response.json())
  .then(data => {
    // display the prediction result in the result element
    resultElement.textContent = data.prediction;
  })
  .catch(error => {
    console.error('Error:', error);
  });
});