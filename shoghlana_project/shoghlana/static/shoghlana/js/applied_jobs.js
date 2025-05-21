// document.addEventListener("DOMContentLoaded", function () {
//   const jobsContainer = document.querySelector(".jobs-container");
//   let appliedJobs = JSON.parse(localStorage.getItem("appliedJobs")) || [];

//   function renderJobs() {
//       jobsContainer.innerHTML = ""; 
//       if (appliedJobs.length === 0) {
//           jobsContainer.innerHTML = "<p>You have not applied to any jobs yet.</p>"; 
//           return;
//       }

//       appliedJobs.forEach(job => {
//           const jobElement = document.createElement("div");
//           jobElement.classList.add("job-card"); 

//           jobElement.innerHTML = `
//               <h2>${job.title}</h2>
//               <p><strong>Company:</strong> ${job.company}</p>
//               <p><strong>Salary:</strong> ${job.salary}$</p>
//               <p><strong>Experience Required:</strong> ${job.experience} year(s)</p>
//               <p><strong>Status:</strong> ${job.status}</p>
//               <p><strong>Description:</strong> ${job.description}</p>
//           `;

//           jobsContainer.appendChild(jobElement);
//       });
//   }

//   renderJobs();
// });
