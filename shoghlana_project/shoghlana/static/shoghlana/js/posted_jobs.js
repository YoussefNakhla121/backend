// document.addEventListener("DOMContentLoaded", function () {
//     const container = document.querySelector(".jobs-container");

//     const jobs = JSON.parse(localStorage.getItem("posted_jobs")) || [];
//     container.innerHTML = "";
//     if (jobs.length === 0) {
//       container.innerHTML = "<p>You have not posted to any jobs yet.</p>"; 
//       return;
//   }
//     jobs.forEach((job) => {
//       const jobCard = document.createElement("div");
//       jobCard.className = "job-card";

//       jobCard.innerHTML = `
//         <h2>${job.title}</h2>
//               <p><strong>Company:</strong> ${job.company}</p>
//               <p><strong>Salary:</strong> ${job.salary}$</p>
//               <p><strong>Experience Required:</strong> ${job.experience} year(s)</p>
//               <p><strong>Status:</strong> ${job.status}</p>
//               <p><strong>Description:</strong> ${job.description}</p>
//       `;
 
//       container.appendChild(jobCard);
//     });
//   });