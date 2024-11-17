// Handle Signup Form Submission
document.getElementById("signupForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const service = document.getElementById("service").value;

  alert(`Thank you for signing up, ${name}! We'll help you find someone to share your ${service} subscription.`);
  // Add logic to send the form data to the server here.
});
