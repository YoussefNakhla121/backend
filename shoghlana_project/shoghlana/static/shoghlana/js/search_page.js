document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".jobs-container");
 
  let searchbar = document.getElementById('search-input');
  let minYears = document.getElementById('min-input');
  let maxYears = document.getElementById('max-input');

  function renderJobs(jobs) {
    container.innerHTML = "";
    if (jobs.length === 0) {
      container.innerHTML = "<p>No jobs found matching your criteria.</p>";
      return;
    }

    jobs.forEach(job => {
      const jobHTML = `
        <div class="job-card">
          <a href="/job_details/${job.id}" class="apply-button">
            <h3>${job.title}</h3>
            <p><b>Company: </b>${job.company}</p>
            <p><b>Years of Experience:</b> ${job.experience} Year(s)</p>
            <p><b>${job.type}</b></p><br>
            <p><b>Description:</b> ${job.description}</p>
            <br/>
            <p><b>Status: </b>${job.status}</p>
          </a>
        </div>`;
      container.innerHTML += jobHTML;
    });
  }

  function fetchJobs() {
    const params = new URLSearchParams({
      title: searchbar.value,
      min_exp: minYears.value,
      max_exp: maxYears.value,
      job_type: document.querySelector('input[name="job-type"]:checked').value
    });

    fetch(`filter_jobs/?${params.toString()}`)
      .then(response => response.json())
      .then(data => renderJobs(data.jobs))
      .catch(error => console.error("Error fetching jobs:", error));
  }

  searchbar.addEventListener("input", fetchJobs);
  minYears.addEventListener("input", fetchJobs);
  maxYears.addEventListener("input", fetchJobs);
  document.querySelectorAll('input[name="job-type"]').forEach(radio => {
    radio.addEventListener("change", fetchJobs);
  });

  fetchJobs();
});
