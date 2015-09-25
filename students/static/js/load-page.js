$(document).ready(function() {
    $('#load-more').click(function() {
        load_more();
    });
});

// AJAX for loading new pages
function load_more() {
     $.ajax({
        url : "", // the endpoint
        type : "GET", // http method
        data : { the_post : $('#post-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json);
            console.log("create post is working!");

            //page += 1
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
