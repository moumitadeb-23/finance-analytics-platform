"use strict";

/* ==========================================================
   FINANCE ANALYTICS PLATFORM
   FinanceAI Assistant
   ChatGPT Style JavaScript
========================================================== */

class FinanceAIChat {

    constructor() {

        /* ==========================================
           STATE
        ========================================== */

        this.messages = [];

        this.currentFile = null;

        this.isTyping = false;

        this.isRecording = false;

        this.currentChart = null;

        this.currentReport = null;

        this.darkMode = false;

        this.sidebarCollapsed = false;

        this.api = {

            chat: "/api/chat",

            chart: "/api/chart",

            report: "/api/report",

            document: "/api/document",

            history: "/api/history",

            reset: "/api/reset",

            status: "/api/status"

        };

        this.initialize();

    }

    /* ==========================================
       INITIALIZE
    ========================================== */

    initialize() {

        this.cacheDOM();

        this.bindEvents();

        this.initializeModals();   

        this.loadTheme();

        this.loadHistory();

        this.checkStatus();

        this.autoResizeTextarea();

    }

    /* ==========================================
       CACHE DOM
    ========================================== */

    cacheDOM() {

        this.chatContainer =
            document.getElementById("messagesContainer");

        this.messageInput =
            document.getElementById("messageInput");

        this.sendButton =
            document.getElementById("sendMessageBtn");

        this.fileInput =
            document.getElementById("fileInput");

        this.attachButton =
            document.getElementById("attachFileBtn");

        this.uploadButton =
            document.getElementById("uploadBtn");

        this.voiceButton =
            document.getElementById("voiceBtn");

        this.voiceRecordButton =
            document.getElementById("voiceRecordBtn");

        this.chartButton =
            document.getElementById("chartBtn");

        this.reportButton =
            document.getElementById("reportBtn");

        this.themeButton =
            document.getElementById("themeBtn");

        this.settingsButton =
            document.getElementById("settingsBtn");

        this.newChatButton =
            document.getElementById("newChatBtn");

        this.typingIndicator =
            document.getElementById("typingIndicator");

        this.filePreview =
            document.getElementById("filePreviewContainer");

        this.progressBar =
            document.getElementById("progressFill");

        this.progressText =
            document.getElementById("progressText");

        this.scrollButton =
            document.getElementById("scrollBottomBtn");

        this.sidebar =
            document.querySelector(".sidebar");

        this.chatHistory =
            document.getElementById("chatHistory");

        this.status =
            document.getElementById("assistantStatus");

    }



    /* ==========================================
       EVENT LISTENERS
    ========================================== */

    bindEvents() {

        /* Send Button */

        this.sendButton?.addEventListener(

            "click",

            () => this.sendMessage()

        );

        /* Enter Key */

        this.messageInput?.addEventListener(

            "keydown",

            (event) => {

                if (

                    event.key === "Enter" &&

                    !event.shiftKey

                ) {

                    event.preventDefault();

                    this.sendMessage();

                }

            }

        );

        /* Auto Resize */

        this.messageInput?.addEventListener(

            "input",

            () => this.autoResizeTextarea()

        );

        /* File Upload */

        this.attachButton?.addEventListener(

            "click",

            () => this.fileInput.click()

        );

        this.uploadButton?.addEventListener(

            "click",

            () => this.fileInput.click()

        );

        this.fileInput?.addEventListener(

            "change",

            (event) => {

                this.handleFile(

                    event.target.files[0]

                );

            }

        );

        /* Theme */

        this.themeButton?.addEventListener(

            "click",

            () => this.toggleTheme()

        );

        /* New Chat */

        this.newChatButton?.addEventListener(

            "click",

            () => this.newChat()

        );

        /* Scroll Button */

        this.scrollButton?.addEventListener(

            "click",

            () => this.scrollBottom()

        );

        /* Sidebar Collapse */

        document.getElementById(

            "collapseSidebar"

        )?.addEventListener(

            "click",

            () => this.toggleSidebar()

        );

        /* Mobile Sidebar */

        document.getElementById(

            "mobileSidebarBtn"

        )?.addEventListener(

            "click",

            () => {

                this.sidebar.classList.toggle(

                    "show"

                );

            }

        );

        /* Search */

        document.getElementById(

            "chatSearch"

        )?.addEventListener(

            "input",

            (event) => {

                this.searchHistory(

                    event.target.value

                );

            }

        );

        /* Voice */

        this.voiceButton?.addEventListener(

            "click",

            () => this.startVoice()

        );

        this.voiceRecordButton?.addEventListener(

            "click",

            () => this.startVoice()

        );

        /* Charts */

        this.chartButton?.addEventListener(

            "click",

            () => this.generateChart()

        );

        /* Reports */

        this.reportButton?.addEventListener(

            "click",

            () => this.generateReport()

        );

        /* Suggestion Cards */

        document

            .querySelectorAll(

                ".suggestion-card"

            )

            .forEach(card => {

                card.addEventListener(

                    "click",

                    () => {

                        this.messageInput.value =

                            card.dataset.prompt;

                        this.sendMessage();

                    }

                );

            });

        /* Drag & Drop */

        this.initializeDragDrop();


        /* Settings */

        this.settingsButton?.addEventListener(

            "click",

            () => {

                window.location.href = "/settings";

            }

        );


        /* ==========================================
        SIDEBAR QUICK ACTIONS
        ========================================== */

        document.getElementById("dashboardBtn")?.addEventListener(
            "click",
            () => window.location.href = "/dashboard"
        );

        document.getElementById("analyticsBtn")?.addEventListener(
            "click",
            () => window.location.href = "/analytics"
        );

        document.getElementById("budgetBtn")?.addEventListener(
            "click",
            () => window.location.href = "/budget-advisor"
        );

        document.getElementById("investmentBtn")?.addEventListener(
            "click",
            () => window.location.href = "/investments"
        );

        document.getElementById("goalsBtn")?.addEventListener(
            "click",
            () => window.location.href = "/goals"
        );

        document.getElementById("notificationBtn")?.addEventListener(
            "click",
            () => window.location.href = "/notifications"
        );

        document.getElementById("uploadDocumentBtn")?.addEventListener(
            "click",
            () => this.fileInput.click()
        );

        document.getElementById("generateChartBtn")?.addEventListener(
            "click",
            () => this.generateChart()
        );

        document.getElementById("generateReportBtn")?.addEventListener(
            "click",
            () => this.generateReport()
        );

        document.getElementById("themeToggle")?.addEventListener(
            "click",
            () => this.toggleTheme()
        );

        document.getElementById("clearConversation")?.addEventListener(
            "click",
            () => this.newChat()
        );


        /* Sidebar Clear Chat */

        document.getElementById("clearConversation")?.addEventListener(

            "click",

            () => {

                this.newChat();

            }

        );


    }


    /* ==========================================
       AUTO RESIZE
    ========================================== */

    autoResizeTextarea() {

        if (!this.messageInput) return;

        this.messageInput.style.height = "auto";

        this.messageInput.style.height =

            this.messageInput.scrollHeight + "px";

    }

    /* ==========================================
       SCROLL TO BOTTOM
    ========================================== */

    scrollBottom() {

        this.chatContainer.scrollTo({

            top: this.chatContainer.scrollHeight,

            behavior: "smooth"

        });

    }

    /* ==========================================
       NEW CHAT
    ========================================== */

    async newChat() {

        const result = await Swal.fire({

            title: "Start New Chat?",

            text: "Current conversation will be cleared.",

            icon: "question",

            showCancelButton: true,

            confirmButtonText: "Start"

        });

        if (!result.isConfirmed) return;

        this.chatContainer.innerHTML = "";

        this.messages = [];

        this.currentFile = null;

        await this.resetConversation();

    }

    /* ==========================================
       SIDEBAR
    ========================================== */

    toggleSidebar() {

        this.sidebar.classList.toggle(

            "collapsed"

        );

    };

    
    /* ==========================================
       SEARCH HISTORY
    ========================================== */

    searchHistory(query) {

        const items =

            this.chatHistory.querySelectorAll(

                ".history-item"

            );

        query = query.toLowerCase();

        items.forEach(item => {

            const text =

                item.textContent.toLowerCase();

            item.style.display =

                text.includes(query)

                    ? "flex"

                    : "none";

        });

    }

    /* ==========================================
       SEND MESSAGE
    ========================================== */

    async sendMessage() {

        const message = this.messageInput.value.trim();

        if (message === "" && !this.currentFile) {

            return;

        }

        /* Hide Welcome Screen */

        const welcome = document.getElementById(

            "welcomeScreen"

        );

        if (welcome) {

            welcome.style.display = "none";

        }

        /* Add User Message */

        this.addUserMessage(message);

        /* Prepare Form Data */

        const formData = new FormData();

        formData.append(

            "message",

            message

        );

        if (this.currentFile) {

            formData.append(

                "file",

                this.currentFile

            );

        }

        /* Reset Input */

        this.messageInput.value = "";

        this.autoResizeTextarea();

        this.showTyping();

        try {

            const response = await fetch(

                this.api.chat,

                {

                    method: "POST",

                    body: formData

                }

            );

            const result = await response.json();

            this.hideTyping();

            if (!result.success) {

                this.addErrorMessage(

                    result.message ||

                    "Something went wrong."

                );

                return;

            }

            this.addAIMessage(

            result.response ||

            result.data ||

            result.message ||

            ""

        );

            if (result.chart) {

                this.addChartCard(

                    result.chart

                );

            }

            if (result.report) {

                this.addReportCard(

                    result.report

                );

            }

            this.currentFile = null;

            this.clearFilePreview();

            this.scrollBottom();

        }

        catch (error) {

            console.error(error);

            this.hideTyping();

            this.addErrorMessage(

                "Unable to connect to FinanceAI."

            );

        }

    }

    /* ==========================================
       USER MESSAGE
    ========================================== */

    addUserMessage(text) {

        const template = document

            .getElementById(

                "userMessageTemplate"

            )

            .content

            .cloneNode(true);

        template.querySelector(

            ".message-text"

        ).textContent = text;

        template.querySelector(

            ".message-time"

        ).textContent =

            new Date().toLocaleTimeString([],{

                hour:"2-digit",

                minute:"2-digit"

            });

        this.chatContainer.appendChild(

            template

        );

        this.scrollBottom();

    }

    /* ==========================================
       AI MESSAGE
    ========================================== */

    addAIMessage(text) {

        const template = document

            .getElementById(

                "aiMessageTemplate"

            )

            .content

            .cloneNode(true);

        const body = template.querySelector(".message-text");

        let html = "";

        // Show uploaded document banner
        const uploadedFileName =
            this.currentFile ? this.currentFile.name : "Uploaded Document";

        html += `
        <div class="document-banner">

        📄 <strong>Analyzed Document:</strong>

        ${uploadedFileName}

        </div>
        `;

        html += marked.parse(text);

        body.innerHTML = html;

        body.querySelectorAll("pre code")

            .forEach(block=>{

                hljs.highlightElement(block);

            });

        template.querySelector(

            ".message-time"

        ).textContent =

            new Date().toLocaleTimeString([],{

                hour:"2-digit",

                minute:"2-digit"

            });

        this.chatContainer.appendChild(

            template

        );

        this.scrollBottom();

    }

    /* ==========================================
       ERROR MESSAGE
    ========================================== */

    addErrorMessage(text) {

        const template = document

            .getElementById(

                "errorTemplate"

            )

            .content

            .cloneNode(true);

        template.querySelector(".message-text").innerHTML = `
        ❌ <b>FinanceAI Error</b><br><br>
        ${text}
        `;

        this.chatContainer.appendChild(

            template

        );

        this.scrollBottom();

    }

    /* ==========================================
       SHOW TYPING
    ========================================== */

    showTyping() {

        this.typingIndicator.classList.remove(

            "hidden"

        );

        this.scrollBottom();

    }

    /* ==========================================
       HIDE TYPING
    ========================================== */

    hideTyping() {

        this.typingIndicator.classList.add(

            "hidden"

        );

    }

        /* ==========================================
       FILE HANDLING
    ========================================== */

    handleFile(file) {

        if (!file) return;

        const maxSize = 20 * 1024 * 1024; // 20 MB

        const allowedTypes = [
            "application/pdf",
            "image/png",
            "image/jpeg",
            "image/jpg",
            "text/csv",
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ];

        if (!allowedTypes.includes(file.type)) {

            Swal.fire({
                icon: "error",
                title: "Unsupported File",
                text: "Please upload PDF, CSV, Excel, JPG or PNG."
            });

            return;
        }

        if (file.size > maxSize) {

            Swal.fire({
                icon: "error",
                title: "File Too Large",
                text: "Maximum allowed size is 20 MB."
            });

            return;
        }

        this.currentFile = file;

        this.showFilePreview(file);

    }

    /* ==========================================
       FILE PREVIEW
    ========================================== */

    showFilePreview(file) {

        this.filePreview.innerHTML = "";

        const template = document

            .getElementById("documentTemplate")

            .content

            .cloneNode(true);

        template.querySelector(

            ".document-name"

        ).textContent = file.name;

        template.querySelector(

            ".document-size"

        ).textContent = this.formatFileSize(

            file.size

        );

        const card = template.querySelector(

            ".uploaded-document"

        );

        const remove = document.createElement("button");

        remove.className = "remove-file";

        remove.innerHTML =

            '<i class="fa-solid fa-xmark"></i>';

        remove.addEventListener(

            "click",

            () => {

                this.clearFilePreview();

            }

        );

        card.appendChild(remove);

        if (

            file.type.startsWith("image/")

        ) {

            const img = document.createElement("img");

            img.className = "image-thumbnail";

            img.src = URL.createObjectURL(file);

            card.prepend(img);

        }

        this.filePreview.appendChild(

            template

        );

    }

    /* ==========================================
       CLEAR FILE
    ========================================== */

    clearFilePreview() {

        this.currentFile = null;

        this.filePreview.innerHTML = "";

        if (this.fileInput) {

            this.fileInput.value = "";

        }

    }

    /* ==========================================
       FORMAT FILE SIZE
    ========================================== */

    formatFileSize(bytes) {

        if (bytes < 1024)

            return bytes + " B";

        if (bytes < 1024 * 1024)

            return (

                bytes / 1024

            ).toFixed(1) + " KB";

        return (

            bytes / (1024 * 1024)

        ).toFixed(2) + " MB";

    }

    /* ==========================================
       DRAG & DROP
    ========================================== */

    initializeDragDrop() {

        const zone = document.getElementById(

            "dropZone"

        );

        if (!zone) return;

        ["dragenter", "dragover"]

            .forEach(eventName => {

                document.addEventListener(

                    eventName,

                    (event) => {

                        event.preventDefault();

                        zone.classList.remove(

                            "hidden"

                        );

                        zone.classList.add(

                            "dragover"

                        );

                    }

                );

            });

        ["dragleave", "drop"]

            .forEach(eventName => {

                document.addEventListener(

                    eventName,

                    (event) => {

                        event.preventDefault();

                        zone.classList.remove(

                            "dragover"

                        );

                        zone.classList.add(

                            "hidden"

                        );

                    }

                );

            });

        zone.addEventListener(

            "drop",

            (event) => {

                const files = event.dataTransfer.files;

                if (

                    files &&

                    files.length > 0

                ) {

                    this.handleFile(

                        files[0]

                    );

                }

            }

        );

    }

    /* ==========================================
       DOCUMENT UPLOAD
    ========================================== */

    async uploadDocument(file) {

        const formData = new FormData();

        formData.append("file", file);

        try {

            const response = await fetch(

                this.api.document,

                {

                    method: "POST",

                    body: formData

                }

            );

            const result = await response.json();

            return result;

        }

        catch (error) {

            console.error(error);

            return {

                success: false,

                message: "Document upload failed."

            };

        }

    }

        /* ==========================================
       VOICE RECOGNITION
    ========================================== */

    startVoice() {

        const SpeechRecognition =
            window.SpeechRecognition ||
            window.webkitSpeechRecognition;

        if (!SpeechRecognition) {

            Swal.fire({
                icon: "error",
                title: "Not Supported",
                text: "Your browser does not support Speech Recognition."
            });

            return;
        }

        const recognition = new SpeechRecognition();

        recognition.lang = "en-US";

        recognition.interimResults = false;

        recognition.maxAlternatives = 1;

        document
            .getElementById("voiceModal")
            ?.classList.remove("hidden");

        recognition.start();

        recognition.onresult = (event) => {

            const transcript =
                event.results[0][0].transcript;

            this.messageInput.value = transcript;

            document
                .getElementById("voiceModal")
                ?.classList.add("hidden");

            this.autoResizeTextarea();

        };

        recognition.onerror = () => {

            document
                .getElementById("voiceModal")
                ?.classList.add("hidden");

            Swal.fire({

                icon: "error",

                title: "Voice Error",

                text: "Unable to recognize speech."

            });

        };

        recognition.onend = () => {

            document
                .getElementById("voiceModal")
                ?.classList.add("hidden");

        };

    }

    /* ==========================================
       THEME
    ========================================== */

toggleTheme() {

    const body = document.body;

    body.classList.toggle("dark");

    const isDark = body.classList.contains("dark");

    localStorage.setItem(
        "finance_theme",
        isDark ? "dark" : "light"
    );

    console.log("Dark Mode:", isDark);
}

    loadTheme() {

        const theme =

            localStorage.getItem(

                "finance_theme"

            );

        if (theme === "dark") {

            document.body.classList.add(

                "dark"

            );

            this.darkMode = true;

        }

    }

    /* ==========================================
       GENERATE CHART
    ========================================== */

    async generateChart() {

        const entity = await Swal.fire({

            title: "Generate Chart",

            input: "select",

            inputOptions: {

                expense: "Expenses",

                income: "Income",

                budget: "Budget",

                investment: "Investments"

            },

            inputPlaceholder: "Select Data",

            showCancelButton: true

        });

        if (!entity.isConfirmed) return;

        try {

            const response = await fetch(

                this.api.chart,

                {

                    method: "POST",

                    headers: {

                        "Content-Type":

                            "application/json"

                    },

                    body: JSON.stringify({

                        entity: entity.value,

                        chart_type: "pie",

                        period: "all"

                    })

                }

            );

            const result =

                await response.json();

            if (!result.success) {

                this.showToast(

                    result.message,

                    "error"

                );

                return;

            }

            this.addChartCard(

                result.data ||

                result.chart

            );

        }

        catch (error) {

            console.error(error);

        }

    }

    /* ==========================================
       GENERATE REPORT
    ========================================== */

    async generateReport() {

        try {

            const response = await fetch(

                this.api.report,

                {

                    method: "POST",

                    headers: {

                        "Content-Type":

                            "application/json"

                    },

                    body: JSON.stringify({

                        report_type:

                            "financial"

                    })

                }

            );

            const result =

                await response.json();

            if (!result.success) {

                this.showToast(

                    result.message,

                    "error"

                );

                return;

            }

            this.addReportCard(

                result.data ||

                result.report

            );

        }

        catch (error) {

            console.error(error);

        }

    }

    /* ==========================================
       LOAD CHAT HISTORY
    ========================================== */

    async loadHistory() {

    const response = await fetch(this.api.history);

    const result = await response.json();

    if (!result.success) return;

    const container = document.getElementById("chatHistory");

    container.innerHTML = "";

    const conversations = [];

    let current = null;

    result.data.forEach(item => {

        if(item.role === "user"){

            current = {
                title: item.content,
                timestamp: item.timestamp,
                user: item.content,
                assistant: ""
            };

            conversations.push(current);

        }

        else if(item.role === "assistant" && current){

            current.assistant = item.content;

        }

    });

    conversations.forEach(chat => {

        this.addHistoryItem(chat);

    });
}

    /* ==========================================
       RESET CONVERSATION
    ========================================== */

    async resetConversation() {

        try {

            await fetch(

                this.api.reset,

                {

                    method: "POST"

                }

            );

        }

        catch (error) {

            console.error(error);

        }

    }

    /* ==========================================
       SYSTEM STATUS
    ========================================== */

    async checkStatus() {

        try {

            const response =

                await fetch(

                    this.api.status

                );

            const result =

                await response.json();

            if (

                result.success

            ) {

                this.status.textContent =

                    "Online";

            }

            else {

                this.status.textContent =

                    "Offline";

            }

        }

        catch {

            this.status.textContent =

                "Offline";

        }

    }

    /* ==========================================
       ADD CHART CARD
    ========================================== */

    addChartCard(chart) {

    const chartUrl =
        typeof chart === "string"
            ? chart
            : chart.path;

    const template = document
        .getElementById("chartTemplate")
        .content
        .cloneNode(true);

    const image = template.querySelector(".generated-chart");

    image.src = chartUrl;

        template.querySelector(
            ".download-chart"
        ).addEventListener(

            "click",

            () => {

                window.open(chartUrl, "_blank");

            }

        );

        template.querySelector(
            ".expand-chart"
        ).addEventListener(

            "click",

            () => {

                document
                    .getElementById("generatedChart")
                    .src = chartUrl;

                document
                    .getElementById("chartModal")
                    .classList.remove("hidden");

            }

        );

        this.chatContainer.appendChild(template);

        this.scrollBottom();

    }

    /* ==========================================
       ADD REPORT CARD
    ========================================== */

    addReportCard(report) {

    const reportUrl =
        typeof report === "string"
            ? report
            : report.path;

    const template = document
        .getElementById("reportTemplate")
        .content
        .cloneNode(true);

    template.querySelector(".download-report")
        .addEventListener("click", () => {

            window.open(reportUrl, "_blank");

        });

    this.chatContainer.appendChild(template);

    this.scrollBottom();

}

    /* ==========================================
       HISTORY ITEM
    ========================================== */

    addHistoryItem(chat) {

    const item = document.createElement("div");

    item.className = "history-item";

    item.innerHTML = `
        <i class="fa-solid fa-message"></i>

        <div class="history-info">
            <div class="history-title">${chat.title}</div>
            <div class="history-time">${chat.timestamp}</div>
        </div>
    `;

    item.addEventListener("click", () => {
        this.loadConversation(chat);
    });

    this.chatHistory.appendChild(item);
}

    loadConversation(chat) {

        this.chatContainer.innerHTML = "";

        this.addUserMessage(chat.user);

        if(chat.assistant){

            this.addAIMessage(chat.assistant);

        }

    }

    /* ==========================================
       TOAST
    ========================================== */

    showToast(message, type = "success") {

        const container = document.getElementById(

            "toastContainer"

        );

        const toast = document.createElement("div");

        toast.className = "toast";

        if (type === "error") {

            toast.style.borderLeftColor = "#dc2626";

        }

        toast.innerHTML = `

            <strong>

                ${type.toUpperCase()}

            </strong>

            <br>

            ${message}

        `;

        container.appendChild(toast);

        setTimeout(() => {

            toast.remove();

        }, 3500);

    }

    /* ==========================================
       COPY TO CLIPBOARD
    ========================================== */

    copy(text) {

        navigator.clipboard.writeText(text);

        this.showToast(

            "Copied to clipboard."

        );

    }

    /* ==========================================
       CLOSE MODALS
    ========================================== */

    initializeModals() {

        document

            .querySelectorAll(

                ".close-modal"

            )

            .forEach(button => {

                button.addEventListener(

                    "click",

                    () => {

                        button

                            .closest(".modal")

                            .classList.add(

                                "hidden"

                            );

                    }

                );

            });

        document

            .querySelectorAll(

                ".modal-overlay"

            )

            .forEach(overlay => {

                overlay.addEventListener(

                    "click",

                    () => {

                        overlay.parentElement

                            .classList.add(

                                "hidden"

                            );

                    }

                );

            });

    }

}

/* ==========================================
   START APPLICATION
========================================== */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        window.financeAI =

            new FinanceAIChat();

    }

);

