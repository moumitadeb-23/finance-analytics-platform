// ======================================================
// FINANCIAL HEALTH DASHBOARD
// Part 1
// ======================================================

document.addEventListener("DOMContentLoaded", function () {

    const dataElement = document.getElementById("dashboard-data");

    if (!dataElement) return;

    const dashboardData = JSON.parse(dataElement.textContent);

    // ==========================================
    // DATA
    // ==========================================

    const healthScore = dashboardData.healthScore || 0;

    const expenseLabels = dashboardData.expenseLabels || [];
    const expenseValues = dashboardData.expenseValues || [];

    const monthLabels = dashboardData.monthLabels || [];
    const monthValues = dashboardData.monthValues || [];

    const totalIncome = dashboardData.totalIncome || 0;
    const totalExpense = dashboardData.totalExpense || 0;

    const investmentValues = dashboardData.investmentValues || [];

    // ==========================================
    // GLOBAL CHART SETTINGS
    // ==========================================

    Chart.defaults.font.family = "Poppins";

    Chart.defaults.font.size = 13;

    Chart.defaults.color = "#64748b";

    Chart.defaults.plugins.legend.labels.usePointStyle = true;

    Chart.defaults.plugins.legend.labels.boxWidth = 10;

    Chart.defaults.animation.duration = 1800;

    Chart.defaults.animation.easing = "easeOutQuart";

    // ==========================================
    // HEALTH SCORE PLUGIN
    // ==========================================

    const centerTextPlugin = {

        id: "centerTextPlugin",

        afterDraw(chart) {

            if (chart.canvas.id !== "healthGauge") return;

            const ctx = chart.ctx;

            const meta = chart.getDatasetMeta(0);

            if (!meta || !meta.data || !meta.data.length) return;

            const x = meta.data[0].x;
            const y = meta.data[0].y;

            ctx.save();

            ctx.textAlign = "center";

            ctx.textBaseline = "middle";

            ctx.fillStyle = "#4f46e5";

            ctx.font = "700 40px Poppins";

            ctx.fillText(healthScore, x, y - 10);

            ctx.fillStyle = "#64748b";

            ctx.font = "15px Poppins";

            ctx.fillText("Health Score", x, y + 22);

            ctx.restore();

        }

    };

    Chart.register(centerTextPlugin);

    // ==========================================
    // HEALTH GAUGE
    // ==========================================

    const gaugeCanvas = document.getElementById("healthGauge");

    if (gaugeCanvas) {

        new Chart(gaugeCanvas, {

            type: "doughnut",

            data: {

                datasets: [

                    {

                        data: [

                            healthScore,

                            100 - healthScore

                        ],

                        backgroundColor: [

                            "#4f46e5",

                            "#e5e7eb"

                        ],

                        borderWidth: 0,

                        borderRadius: 20,

                        hoverOffset: 2

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                cutout: "78%",

                rotation: -90,

                circumference: 360,

                plugins: {

                    legend: {

                        display: false

                    },

                    tooltip: {

                        enabled: false

                    }

                }

            }

        });

    }

        // ==========================================
    // INCOME VS EXPENSE BAR CHART
    // ==========================================

    const incomeExpenseCanvas =
        document.getElementById("incomeExpenseChart");

    if (incomeExpenseCanvas) {

        const incomeGradient =
            incomeExpenseCanvas.getContext("2d")
            .createLinearGradient(0,0,0,350);

        incomeGradient.addColorStop(0,"#6366f1");
        incomeGradient.addColorStop(1,"#4338ca");

        const expenseGradient =
            incomeExpenseCanvas.getContext("2d")
            .createLinearGradient(0,0,0,350);

        expenseGradient.addColorStop(0,"#ef4444");
        expenseGradient.addColorStop(1,"#dc2626");

        new Chart(incomeExpenseCanvas,{

            type:"bar",

            data:{

                labels:["Income","Expense"],

                datasets:[{

                    data:[
                        totalIncome,
                        totalExpense
                    ],

                    backgroundColor:[
                        incomeGradient,
                        expenseGradient
                    ],

                    borderRadius:16,

                    borderSkipped:false,

                    maxBarThickness:70

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{
                        display:false
                    },

                    tooltip:{

                        callbacks:{

                            label:function(context){

                                return "₹ " +
                                context.raw.toLocaleString();

                            }

                        }

                    }

                },

                scales:{

                    x:{

                        grid:{
                            display:false
                        }

                    },

                    y:{

                        beginAtZero:true,

                        grid:{
                            color:"#edf2f7"
                        },

                        ticks:{

                            callback:function(value){

                                return "₹"+value;

                            }

                        }

                    }

                }

            }

        });

    }

    // ==========================================
    // EXPENSE BREAKDOWN
    // ==========================================

    const expenseCanvas =
        document.getElementById("expenseChart");

    if(expenseCanvas){

        const totalExpenseAmount =
            expenseValues.reduce((a,b)=>a+b,0);

        const centerExpenseText={

            id:"centerExpenseText",

            afterDraw(chart){

                if(chart.canvas.id!=="expenseChart")
                    return;

                const ctx=chart.ctx;

                const meta=chart.getDatasetMeta(0);

                const x=meta.data[0].x;
                const y=meta.data[0].y;

                ctx.save();

                ctx.textAlign="center";

                ctx.fillStyle="#111827";

                ctx.font="700 24px Poppins";

                ctx.fillText(

                    "₹"+totalExpenseAmount.toLocaleString(),

                    x,

                    y-5

                );

                ctx.fillStyle="#6b7280";

                ctx.font="14px Poppins";

                ctx.fillText(

                    "Expenses",

                    x,

                    y+22

                );

                ctx.restore();

            }

        };

        Chart.register(centerExpenseText);

        new Chart(expenseCanvas,{

            type:"doughnut",

            data:{

                labels:expenseLabels,

                datasets:[{

                    data:expenseValues,

                    backgroundColor:[

                        "#4f46e5",

                        "#8b5cf6",

                        "#06b6d4",

                        "#10b981",

                        "#f59e0b",

                        "#ef4444",

                        "#ec4899",

                        "#14b8a6"

                    ],

                    borderWidth:0,

                    hoverOffset:12

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false,

                cutout:"72%",

                plugins:{

                    legend:{

                        position:"bottom",

                        labels:{

                            padding:18,

                            usePointStyle:true

                        }

                    }

                }

            }

        });

    }

        // ==========================================
    // SAVINGS TREND
    // ==========================================

    const savingCanvas =
        document.getElementById("savingChart");

    if (savingCanvas) {

        const ctx = savingCanvas.getContext("2d");

        const gradient = ctx.createLinearGradient(0, 0, 0, 350);

        gradient.addColorStop(0, "rgba(79,70,229,.35)");
        gradient.addColorStop(1, "rgba(79,70,229,0)");

        new Chart(savingCanvas, {

            type: "line",

            data: {

                labels: monthLabels,

                datasets: [{

                    label: "Savings",

                    data: monthValues,

                    borderColor: "#4f46e5",

                    backgroundColor: gradient,

                    fill: true,

                    tension: .45,

                    borderWidth: 4,

                    pointRadius: 5,

                    pointHoverRadius: 8,

                    pointBackgroundColor: "#ffffff",

                    pointBorderColor: "#4f46e5",

                    pointBorderWidth: 3

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {

                        display: false

                    }

                },

                scales: {

                    x: {

                        grid: {

                            display: false

                        }

                    },

                    y: {

                        beginAtZero: false,

                        grid: {

                            color: "#edf2f7"

                        },

                        ticks: {

                            callback: value => "₹" + value

                        }

                    }

                }

            }

        });

    }

    // ==========================================
    // INVESTMENT PERFORMANCE
    // ==========================================

    const investmentCanvas =
        document.getElementById("investmentChart");

    if (investmentCanvas) {

        const ctx = investmentCanvas.getContext("2d");

        const gradient = ctx.createLinearGradient(0,0,0,350);

        gradient.addColorStop(0,"rgba(139,92,246,.35)");
        gradient.addColorStop(1,"rgba(139,92,246,0)");

        new Chart(investmentCanvas,{

            type:"line",

            data:{

                labels:monthLabels,

                datasets:[{

                    label:"Investment",

                    data:investmentValues,

                    borderColor:"#8b5cf6",

                    backgroundColor:gradient,

                    fill:true,

                    tension:.45,

                    borderWidth:4,

                    pointRadius:5,

                    pointHoverRadius:8,

                    pointBackgroundColor:"#ffffff",

                    pointBorderColor:"#8b5cf6",

                    pointBorderWidth:3

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{

                        display:false

                    }

                },

                scales:{

                    x:{

                        grid:{

                            display:false

                        }

                    },

                    y:{

                        beginAtZero:false,

                        grid:{

                            color:"#edf2f7"

                        },

                        ticks:{

                            callback:value=>"₹"+value

                        }

                    }

                }

            }

        });

    }

}); // DOMContentLoaded ends here