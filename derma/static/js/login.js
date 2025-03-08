 // Slideshow functionality
 const slides = document.querySelectorAll('.slide');
 const indicators = document.querySelectorAll('.indicator');
 let currentSlide = 0;
 const slideInterval = 5000; // Change slide every 5 seconds
 
 function showSlide(index) {
     slides.forEach(slide => slide.classList.remove('active'));
     indicators.forEach(indicator => indicator.classList.remove('active'));
     
     slides[index].classList.add('active');
     indicators[index].classList.add('active');
     currentSlide = index;
 }
 
 // Handle indicator clicks
 indicators.forEach(indicator => {
     indicator.addEventListener('click', () => {
         const index = parseInt(indicator.getAttribute('data-index'));
         showSlide(index);
         resetInterval();
     });
 });
 
 // Auto-advance slides
 let slideTimer = setInterval(() => {
     currentSlide = (currentSlide + 1) % slides.length;
     showSlide(currentSlide);
 }, slideInterval);
 
 function resetInterval() {
     clearInterval(slideTimer);
     slideTimer = setInterval(() => {
         currentSlide = (currentSlide + 1) % slides.length;
         showSlide(currentSlide);
     }, slideInterval);
 }
 
 // Password visibility toggle
 const passwordToggle = document.querySelector('.password-toggle');
 const passwordInput = document.querySelector('input[type="password"]');
 
 passwordToggle.addEventListener('click', () => {
     if (passwordInput.type === 'password') {
         passwordInput.type = 'text';
         passwordToggle.innerHTML = `
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                 <path d="M1 12C1 12 5 4 12 4C19 4 23 12 23 12C23 12 19 20 12 20C5 20 1 12 1 12Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                 <path d="M12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                 <path d="M2 2L22 22" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
             </svg>
         `;
     } else {
         passwordInput.type = 'password';
         passwordToggle.innerHTML = `
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                 <path d="M1 12C1 12 5 4 12 4C19 4 23 12 23 12C23 12 19 20 12 20C5 20 1 12 1 12Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                 <path d="M12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
             </svg>
         `;
     }
 });