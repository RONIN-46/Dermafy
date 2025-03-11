document.addEventListener("DOMContentLoaded", function () {
    const otpForm = document.getElementById("otpForm");
    const verifyOtpForm = document.getElementById("verifyOtpForm");

    otpForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const email = document.getElementById("email").value;

        if (email) {
            alert("OTP sent to " + email);
            otpForm.style.display = "none";
            verifyOtpForm.style.display = "block";
        }
    });

    verifyOtpForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const otp = document.getElementById("otp").value;

        if (otp.length === 6) {
            alert("OTP Verified Successfully!");
        } else {
            alert("Invalid OTP. Please try again.");
        }
    });
});
