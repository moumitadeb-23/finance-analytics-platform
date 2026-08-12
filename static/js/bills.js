// ======================================================
// Bills & Subscriptions
// ======================================================

document.addEventListener("DOMContentLoaded", function () {

    // ==========================================
    // Live Search
    // ==========================================

    const searchInput = document.getElementById("searchBill");
    const table = document.getElementById("billTable");

    if (searchInput && table) {

        searchInput.addEventListener("keyup", function () {

            const value = this.value.toLowerCase();

            const rows = table.querySelectorAll("tbody tr");

            rows.forEach(row => {

                const text = row.innerText.toLowerCase();

                row.style.display =
                    text.includes(value) ? "" : "none";

            });

        });

    }

    // ==========================================
    // Highlight Due Dates
    // ==========================================

    const rows = document.querySelectorAll("#billTable tbody tr");

    rows.forEach(row => {

        const dueCell = row.cells[3];

        if (!dueCell) return;

        const dueDate = new Date(dueCell.innerText);

        const today = new Date();

        today.setHours(0,0,0,0);

        const diffDays = Math.ceil(
            (dueDate - today) / (1000 * 60 * 60 * 24)
        );

        if (isNaN(diffDays)) return;

        if (diffDays < 0) {

            row.style.background = "#ffe5e5";

        }

        else if (diffDays <= 3) {

            row.style.background = "#fff7d6";

        }

    });

    // ==========================================
    // Confirm Delete
    // ==========================================

    document.querySelectorAll(".btn-danger").forEach(btn => {

        btn.addEventListener("click", function (e) {

            const ok = confirm(
                "Are you sure you want to delete this bill?"
            );

            if (!ok) {

                e.preventDefault();

            }

        });

    });

    // ==========================================
    // Console
    // ==========================================

    console.log(
        "✅ Bills & Subscriptions Loaded Successfully"
    );

});

