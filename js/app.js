function mouseover() {
    if (this.getAnimation() == null || typeof this.getAnimation() === "undefined") {

        /* 
        Because of the google maps bug of moving cursor several times over and out of marker
        causes bounce animation to break - we use small timer before triggering the bounce animation
        */
        
        clearTimeout(bounceTimer);
        
        var that = this;
         
        bounceTimer = setTimeout(function(){
             that.setAnimation(google.maps.Animation.BOUNCE);
        },
        500);

    }
}

function mouseout() {
    if (this.getAnimation() != null) {
        this.setAnimation(null);
    }

    // If we already left marker, no need to bounce when timer is ready
    clearTimeout(bounceTimer);
}