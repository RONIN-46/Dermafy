const quizContainer = document.getElementById("quiz");
const questionEl = document.getElementById("question");
const optionsEl = document.getElementById("options");
const nextBtn = document.getElementById("next-btn");

let currentQuestionIndex = 0;
let userResponses = [];

// ✅ Model fields (in order) matching Django model
const fields = [
    "primary_skin_concern", "skin_type", "breakout_frequency", "reaction_to_skincare",
    "redness_inflammation", "sunscreen_usage", "skin_conditions", "after_washing_skin_feel",
    "water_intake", "dark_spots_pigmentation", "visible_pores", "exfoliation_frequency",
    "fine_lines_wrinkles", "dairy_processed_food_intake", "skincare_routine"
];

// ✅ Questions and options
const questions = [
    "What is your primary skin concern?",
    "What is your skin type?",
    "How often do you experience breakouts?",
    "How does your skin react to skincare products?",
    "Do you experience redness or inflammation?",
    "How often do you use sunscreen?",
    "Do you have any existing skin conditions?",
    "How does your skin feel after washing?",
    "What is your daily water intake?",
    "Do you have dark spots or pigmentation?",
    "Do you notice visible pores?",
    "How often do you exfoliate?",
    "Do you have fine lines or wrinkles?",
    "How often do you consume dairy or processed food?",
    "Describe your skincare routine:"
];

const options = [
    ["Acne", "Dryness", "Redness", "Other"],
    ["Oily", "Dry", "Combination", "Normal"],
    ["Rarely", "Sometimes", "Frequently", "Daily"],
    ["No reaction", "Slight redness", "Severe irritation", "Other"],
    ["No", "Sometimes", "Yes", "Other"],
    ["Never", "Rarely", "Often", "Daily"],
    ["Eczema", "Psoriasis", "Acne", "None"],
    ["Tight", "Oily", "Dry", "Normal"],
    ["Less than 1L", "1-2L", "2-3L", "More than 3L"],
    ["No", "Yes", "Mild", "Severe"],
    ["No", "Yes", "Slightly", "Prominent"],
    ["Never", "Rarely", "Often", "Daily"],
    ["No", "Yes", "Slightly", "Prominent"],
    ["Never", "Sometimes", "Often", "Daily"],
    ["Minimal", "Basic", "Extensive", "Other"]
];

// ✅ Load current question and options
function loadQuestion() {
    const currentQuestion = questions[currentQuestionIndex];
    const currentOptions = options[currentQuestionIndex];

    // ✅ Set question text
    questionEl.textContent = currentQuestion;

    // ✅ Clear previous options
    optionsEl.innerHTML = "";

    // ✅ Render options dynamically
    currentOptions.forEach((option) => {
        const optionButton = document.createElement("button");
        optionButton.classList.add("btn");
        optionButton.textContent = option;

        // ✅ Add "name" attribute to align with Django fields
        optionButton.setAttribute("name", fields[currentQuestionIndex]);

        optionButton.addEventListener("click", () => handleOptionSelect(option, optionButton));
        optionsEl.appendChild(optionButton);
    });

    // ✅ Show next button if it's not the last question
    nextBtn.style.display = (currentQuestionIndex < questions.length - 1) ? "block" : "none";
}

// ✅ Handle option selection
function handleOptionSelect(option, button) {
    // ✅ Save the selected response
    userResponses[currentQuestionIndex] = option;

    // ✅ Remove highlight from previous selection
    optionsEl.querySelectorAll(".btn").forEach((btn) => btn.classList.remove("selected"));

    // ✅ Highlight selected option
    button.classList.add("selected");

    };

// ✅ Show submit button after last question
function showSubmitButton() {
    nextBtn.style.display = "none"; // Hide next button

    const submitBtn = document.createElement("button");
    submitBtn.textContent = "Submit Quiz";
    submitBtn.classList.add("btn");
    submitBtn.style.backgroundColor = "#4CAF50";

    submitBtn.addEventListener("click", submitQuiz);
    quizContainer.appendChild(submitBtn);
}

// ✅ Submit quiz data to Django backend
function submitQuiz(event) {
    event.preventDefault();

    const formData = new FormData();

    // ✅ Add CSRF token for Django security
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    formData.append('csrfmiddlewaretoken', csrfToken);

    // ✅ Map user responses to correct fields
    fields.forEach((field, index) => {
        formData.append(field, userResponses[index] || "");
    });

    // ✅ Send data using POST request
    fetch("/submit_quiz/", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "/dashboard/"; // Redirect after submission
        } else {
            console.error("Failed to submit quiz");
            alert("Failed to submit quiz. Please try again.");
        }
    })
    .catch(error => {
        console.error("Error submitting quiz:", error);
        alert("Error submitting quiz. Please try again.");
    });
}

// ✅ Handle next button click manually
nextBtn.addEventListener("click", (e) => {
    e.preventDefault();
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        loadQuestion();
    } else {
        showSubmitButton();
    }
});

// ✅ Load quiz on page load
document.addEventListener("DOMContentLoaded", loadQuestion);
