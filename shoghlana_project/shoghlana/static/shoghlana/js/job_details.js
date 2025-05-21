// document.addEventListener("DOMContentLoaded", function () {
//     const statusElement = document.querySelector(".job_status");
//     const applyButton = document.querySelector(".apply_button");

//     if (statusElement && applyButton) {
//         const statusText = statusElement.textContent.toLowerCase();


//         if (statusText.includes("closed")) {
//             applyButton.style.display = "none";
//         }


//         const appliedJobs = JSON.parse(localStorage.getItem("appliedJobs")) || [];
//         const alreadyApplied = appliedJobs.some(job => job.title === jobTitle && job.company === companyName);

//         if (alreadyApplied) {
//             applyButton.style.display = "none";
//         }


//         applyButton.addEventListener("click", function () {
//             const newJob = {
//                 title: jobTitle,
//                 company: companyName,
//                 salary: salary,
//                 experience: experience,
//                 status: status,
//                 description: description,
//             };

//             appliedJobs.push(newJob);
//             localStorage.setItem("appliedJobs", JSON.stringify(appliedJobs));

//             applyButton.style.display = "none";
//             window.location.href = "applied_jobs.html";
//         });
//     }
// });

// const userType = localStorage.getItem('userType');

// if (userType === 'Admin') {
//     const apply_button = document.getElementById('apply_button');
//     apply_button.style.display = 'none';
// }
