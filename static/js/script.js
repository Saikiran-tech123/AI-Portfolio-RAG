// ==========================================
// AI SEARCH
// ==========================================

const searchButton = document.getElementById("searchButton");
const searchInput = document.getElementById("searchInput");
const searchResult = document.getElementById("searchResult");


async function performSearch() {

    const query = searchInput.value.trim();

    if (query === "") {

        searchResult.innerHTML = `
            <div class="ai-title">🤖 AI Answer</div>
            <div class="ai-response">
                Please enter a question.
            </div>
        `;

        return;
    }


    // Show loading
    searchResult.innerHTML = `
        <div class="ai-title">🤖 AI Answer</div>
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
                query: query
            })

        });


        const data = await response.json();


        console.log("API RESPONSE:", data);


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

        console.error("SEARCH ERROR:", error);

        searchResult.innerHTML = `
            <div class="ai-title">
                ❌ Connection Error
            </div>

            <div class="ai-response">
                Could not connect to the Flask backend.
            </div>
        `;

    }

}


// Search button
searchButton.addEventListener(
    "click",
    performSearch
);


// Enter key
searchInput.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {

            performSearch();

        }

    }
);