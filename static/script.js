async function analyzeMessage() {

    const message =
        document.getElementById("messageInput").value.trim();

    const errorMessage =
        document.getElementById("errorMessage");

    errorMessage.textContent = "";

    if (!message) {

        errorMessage.textContent =
            "Please enter a message.";

        return;
    }


    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (!response.ok) {

            errorMessage.textContent =
                data.error || "Something went wrong.";

            return;
        }


        // Priority

        const priorityElement =
            document.getElementById("priority");

        priorityElement.textContent =
            data.priority;

        priorityElement.className =
            "result-value " +
            data.priority.toLowerCase();


        // Priority confidence

        document.getElementById(
            "priorityConfidence"
        ).textContent =
            "Confidence: " +
            data.priority_confidence +
            "%";


        // Category

        document.getElementById(
            "category"
        ).textContent =
            data.category;


        // Category confidence

        document.getElementById(
            "categoryConfidence"
        ).textContent =
            "Confidence: " +
            data.category_confidence +
            "%";


        // Recommended action

        document.getElementById(
            "action"
        ).textContent =
            data.recommended_action;


        // Important factors

        const factorsList =
            document.getElementById("factorsList");

        factorsList.innerHTML = "";


        data.important_factors.forEach(
            function(factor) {

                const li =
                    document.createElement("li");

                li.textContent = factor;

                factorsList.appendChild(li);

            }
        );


    } catch (error) {

        errorMessage.textContent =
            "Unable to connect to the server.";

        console.error(error);
    }
}