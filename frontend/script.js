document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");
    const searchButton = document.getElementById("searchButton");
    const searchResult = document.getElementById("searchResult");

    console.log("JavaScript loaded successfully");


    async function searchPortfolio() {

        const question = searchInput.value.trim();

        if (question === "") {
            searchResult.innerHTML = `
                <div class="ai-title">
                    🤖 AI Answer
                </div>

                <div class="ai-response">
                    Please enter a question.
                </div>
            `;
            return;
        }


        // Show searching message
        searchResult.innerHTML = `
            <div class="ai-title">
                🤖 AI Answer
            </div>

            <div class="ai-response">
                Searching...
            </div>
        `;


        try {

            const response = await fetch("/api/search", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    query: question
                })

            });


            const data = await response.json();

            console.log("Backend response:", data);


            if (data.status === "success") {

                searchResult.innerHTML = `
                    <div class="ai-title">
                        🤖 AI Answer
                    </div>

                    <div class="ai-response">
                        ${data.answer.replace(/\n/g, "<br>")}
                    </div>
                `;

            } else {

                searchResult.innerHTML = `
                    <div class="ai-title">
                        ❌ Error
                    </div>

                    <div class="ai-response">
                        ${data.message}
                    </div>
                `;

            }


        } catch (error) {

            console.error("Error:", error);

            searchResult.innerHTML = `
                <div class="ai-title">
                    ❌ Connection Error
                </div>

                <div class="ai-response">
                    Unable to connect to the backend.
                </div>
            `;

        }

    }


    // Search button
    searchButton.addEventListener(
        "click",
        searchPortfolio
    );


    // Press Enter
    searchInput.addEventListener(
        "keydown",
        function (event) {

            if (event.key === "Enter") {
                searchPortfolio();
            }

        }
    );

});