import React from "react";
import "./TeamStockChart.css";
import { Line } from "react-chartjs-2";
import Chart from "chart.js/auto";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchStockChartData, fetchStockDetails } from "../../Utils";
import { addCommas } from "../../Utils";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";


function TeamStockChart({ oddsHistory }) {
  const dispatch = useDispatch();
  const linkHistory = useHistory();
  const [stockChartData, setStockChartData] = useState(null);
  const [dateRange, setDateRange] = useState(90);
  const [currentPrice, setCurrentPrice] = useState(0);
  const [stockName, setStockName] = useState("");
  const [isActive, setActive] = useState(false);
    const [rangeText, setRangeText] = useState("All Time");

    let oddsHistoryArray;
    if (oddsHistory) {
      oddsHistoryArray = Object.values(oddsHistory);
    }
    console.log("oddsHistoryArray", oddsHistoryArray);

  useEffect(() => {
    if (!oddsHistory) {
      return;
    }


      // const labels = ["5/14/2023", "6/14/2023", "7/14/2023", "8/20/2023"];
    const prices = [12.5, 5.5, 6.8, 7.5]
    const labels = oddsHistoryArray.map((data) =>    //!! NOTE: DON'T RENAME. Must be names labels for some reason
      new Date(data.date).toLocaleDateString()
    );
    const prices2 = oddsHistoryArray.map((data) => data.price);

    console.log("dates2", labels)
      console.log("prices2", prices2);


      setStockChartData({
        labels,
        datasets: [
          {
            data: prices2,
            backgroundColor: "none",
            borderColor: "#00C805",
            borderWidth: 2,
            pointBorderColor: "rgba(0, 0, 0, 0)",
            pointBackgroundColor: "rgba(0, 0, 0, 0)",
            pointHoverBackgroundColor: "#00C805",
            pointHoverBorderColor: "#000000",
            pointHoverBorderWidth: 4,
            pointHoverRadius: 6,
            tension: 0.0,
            fill: false,
          },
        ],
      });


  }, [dateRange, oddsHistory]);



  // Chart.js options
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {
        grid: {
          display: false,
          drawOnChartArea: false,
          drawBorder: false,
        },
        ticks: {
          display: false,
        },
      },
      y: {
        grid: {
          display: false,
          drawOnChartArea: false,
          drawBorder: false,
        },
        ticks: {
          display: false,
        },
      },
    },
    plugins: {
      legend: false,
    },
  };


  const toggleClass = () => {
    setActive(!isActive);
  };



  return (
    <div className="chart-container">

      <div className="line-chart">
        {stockChartData && <Line data={stockChartData} options={options} />}
      </div>
      <div className="timeline-container">
        <div className="timeline-buttons-container">
          <div
            className={`timeline-button ${dateRange === 7 ? "active" : ""}`}
            onClick={() => {
              setDateRange(7);
              toggleClass();
            }}
          >
            1W
          </div>
          <div
            className={`timeline-button ${dateRange === 30 ? "active" : ""}`}
            onClick={() => {
              setDateRange(30);
              toggleClass();
            }}
          >
            1M
          </div>
          <div
            name="3M"
            className={`timeline-button ${dateRange === 90 ? "active" : ""}`}
            onClick={() => {
              setDateRange(90);
              toggleClass();
            }}
          >
            3M
          </div>
          <div
            className={`timeline-button ${dateRange === 365 ? "active" : ""}`}
            onClick={() => {
              setDateRange(365);
              toggleClass();
            }}
          >
            1Y
          </div>
          <div
            className={`timeline-button ${
              dateRange === 365 * 5 ? "active" : ""
            }`}
            onClick={() => {
              setDateRange(365 * 5);
              toggleClass();
            }}
          >
            ALL
          </div>
        </div>
      </div>

    </div>
  );
}

export default TeamStockChart;
