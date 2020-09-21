$(document).ready(() => {
  // $('#searchForm').on('click', (e) => {
    var searchText = $('#searchText').text();
    console.log("oey :"+searchText);
    getMovies(searchText);
    // e.preventDefault();
  // });
});

function getMovies(searchText){
  axios.get("http://api.tvmaze.com/singlesearch/shows?q="+ searchText)
    .then((response) => {
      console.log(response);
      let movies = response.data;
      let output = '';

        output += `
        <a href="${movies.officialSite}">
          <img class="row__poster" src='https://yt3.ggpht.com/a/AATXAJyzyrPJMwSCUxtTlY-MQ9sEqX8XHm8MYq4yr7e6Gw=s900-c-k-c0xffffffff-no-rj-mo' width="50" height="60" alt="netflix"></a>
        `;

        $('#movies').html(output);
      })
      .catch((err) => {
        console.log(err);
      });
  }
  // <div class="well text-center">
  //   <img src="${movies.image.medium}">
  //   <h5>${movies.name}</h5>
