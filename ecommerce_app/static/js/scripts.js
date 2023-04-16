$(document).ready(function(){
	$('.image-main').slick({
      dots: true,
      arrows: false,
      autoplay: true,
      autoplaySpeed: 2500, 
      infinite: true
    });
  });



  $(document).ready(function(){
    $('.cards-main').slick({
      dots: true,
      arrows: true,
      slidesToShow: 5, 
      slidesToScroll: 1, 
    });
  });

const form =  document.querySelector("#search-input");
const search = document.querySelector(".prod-search")
form.addEventListener("input", function(event){
	event.preventDefault()
	console.log("aqui")

	const formSearch = document.querySelector('.form-search');
  	const formData = new FormData(formSearch);
  	const csrfToken = formData.get('csrfmiddlewaretoken');

  	formData.append('csrfmiddlewaretoken', csrfToken);

 	url = "/searchForm/";
  	fetch(url, {
  	  method: 'POST',
  	  headers: {
  	    'X-CSRFToken': csrfToken
  	  },
  	  body: JSON.stringify({
  	    'querry': form.value,
  	  }),
	}).then(response => response.json())
	.then(data => {
		search.innerHTML = data.html_results;
	});
})	
