---
---
var Alert    =
{
  RESPONSE_DELIVERY_SUCCESS:
  {
      title: "Response Delivered!",
    content: "Your response has been delivered. We will get in touch with you shortly.",
       icon: { src: "{{ site.urls.icons }}/happy.png" }
  },
  RESPONSE_DELIVERY_FAILURE:
  {
      title: "Whoops!",
    content: "An error occured while attempting to submit your response. Please try again.",
       icon: { src: "{{ site.urls.icons }}/sad.png" }
  }
};
var PRODUCTS = [
  {% for product in site.data.products %}
    {{ product | jsonify }},
  {% endfor %}
];

function randint(offset) {
  var random = Math.floor(Math.random() * offset)

  return random
};

function setupGallery ( ) {
  var sources = [ ]
  {% for item in site.data.images.gallery %}
    sources.push("{{ item.src }}");
  {% endfor %}

  var $cells  = $(".gallery-cell").children("img").filter(":visible");
  $cells.each(function (i) {
    $(this).data("original", sources[i])
           .attr("src", sources[i])
  });

  var pool    = [ ]
  for (var i  = $cells.length ; i < sources.length ; ++i)
    pool.push(sources[i])

  var next    = 0
  setInterval(function ( ) {
    var $element = $cells.eq(randint($cells.length));
    var previous = $element.attr("src");

    var source   = pool[next];

    pool.splice(next, 1);
    pool.push(previous);

        next     = (next + 1) % pool.length;

    $element.fadeOut(1500, function ( ) {
      $element.attr("src", source)
              .fadeIn(1500);
    });
  }, 5000);
}

function displayAlert (alert) {
  $(".modal-info-head").html(alert.title);
  $(".modal-info-body").html(alert.content);
  $(".modal-info-icon").attr("src", alert.icon.src);

  $(".modal-info").modal("show");
};

// function renderFancyBorder ( ) {
//   $(".fancyborder").each(function ( ) {
//     var $element  = $(this)
//     ,   $parent   = $(this).parent()
//     ,   width     = $parent.width()
//     ,   height    = $element.data("height") || 50
//     ,   border    = $element.data("border")
//     ,   color     = $element.data("color")  || "rgb(0, 0, 0)"
//     ,   positions = Array.from(border);
//
//     if ( positions.includes("t") ) {
//       $element.css("border-bottom", height + "px solid " + color);
//     }
//
//     if ( positions.includes("b") ) {
//       $element.css("border-top",    height + "px solid " + color);
//     }
//
//     if ( positions.includes("r") ) {
//       $element.css("border-left",   width  + "px solid transparent");
//     }
//   });
// };

function sendEmail (email, data, callback) {
  // calback(success, error)
  $.ajax({
    url: "https://formspree.io/" + email,
    method: "POST",
    data: data,
    dataType: "json",
    success: function (response) {
      if ( response.success == "email sent" ) {
        callback(true);
      } else {
        console.log('ERROR: formspree.io email address not confirmed.');

        callback(false);
      }
    },
    error: function (xhr, status, err) {
      callback(false);
    }
  });
};

function getProductByID (ID) {
  for (var i = 0 ; i < PRODUCTS.length ; ++i) {
    if ( PRODUCTS[i]['ID'] == ID ) {
      return PRODUCTS[i];
    }
  }
}

function displayProduct (product) {
  $(".product").data("product", product.ID);

  // view
  $(".product-name").html(product.name);

  // details
  var size      = product.size;
  $(".product-size").html(size.width + ' x ' + size.height);
  $(".product-medium").html(product.medium.join(", "));
  $(".product-type").html(product.type);

  // price
  var price     = product.price;
  var value     = price.value;

  var select    = $(".product-select").selectpicker("val");
  var thumbnail;

  if ( product.frame ) {
    $(".product-select").prop("disabled", false);
    $(".product-select").selectpicker("refresh");

    $("form.fproduct-frame").removeClass("hidden");

    var frame   = product.frame;

    if ( select == "frame" ) {
      thumbnail = product.image.src + "/frame.jpg";

      if ( price.currency.code == frame.price.currency.code ) {
        value  += frame.price.value;
      }
    } else {
      thumbnail = product.image.src + "/no-frame.jpg";
    }

    $(".product-frame-paypal-ID").val(frame.paypal.ID);
  } else {
    $(".product-select").val("no-frame");

    $(".product-select").prop("disabled", true);
    $(".product-select").selectpicker("refresh");

    $("form.fproduct-frame").addClass("hidden");

    thumbnail   = product.image.src + "/no-frame.jpg";
  }

  value         = value.toLocaleString(undefined, { maximumFractionDigits: 2 })

  $(".product-thumbnail").attr("src", thumbnail);

  $(".product-price-currency").html(price.currency.symbol);
  $(".product-price-value").html(value);

  $(".product-paypal-ID").val(product.paypal.ID);
}

function setupStore ( ) {
  for (var i = 0 ; i < PRODUCTS.length ; ++i) {
    var product = PRODUCTS[i];
    $(".slick-store").append(
      '<a href="javascript:void(0);" class="slick-product"                      \
        data-product="' + product.ID + '">                                      \
        <div class="panel panel-default no-background no-border no-shadow       \
          no-margin">                                                           \
          <img class="center-block" height="200" src="'
            + product.image.src + "/no-frame.jpg" + '">                         \
          <div class="text-center">                                             \
            <h5 class="text-uppercase visible-lg">                              \
              ' + product.name + '                                              \
            </h5>                                                               \
          </div>                                                                \
        </div>                                                                  \
      </a>'
    );
  };

  $(".slick-product").click(function ( ) {
    var $element = $(this)
    ,   ID       = $element.data('product')
    ,   product  = getProductByID(ID);

    displayProduct(product);
  });

  $(".product-select").on("change", function ( ) {
    var ID       = $(".product").data("product")
    ,   product  = getProductByID(ID);

    displayProduct(product);
  });

  $(".slick-store").on("init afterChange", function (event, slick, current, next) {
    var current  = current ? current : 0
    ,   $element = $(slick.$slides.get(current))
    ,   ID       = $element.data('product')
    ,   product  = getProductByID(ID);

    displayProduct(product);
  });

  $(".slick-store").slick({
      slidesToShow: 5,
    slidesToScroll: 1,
         prevArrow: '<img class="a-left control-c prev slick-prev" src="{{ site.urls.icons }}/chevron-left.png">',
         nextArrow: '<img class="a-right control-c next slick-next" src="{{ site.urls.icons }}/chevron-right.png">',
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
  });
};

$(document).ready(function ( ) {
  $('.loader-skip').click(hideLoader);

  if ( $('.navbar-fixed-top').length ) {
    $('body').css('padding-top', '50px');
  }

  // smoothScroll
  smoothScroll.init({
    selectorHeader: "[data-scroll-header]",
    speed: 1000,
    easing: "easeInOutQuint"
  });

  // lazyload
  $("img.lazy").lazyload({
    effect: "fadeIn"
  });

  // gallery
  setupGallery();

  // fancyborder
  // renderFancyBorder();

  $(".copyright-date").each(function ( ) {
    var $element = $(this)
    ,   today    = new Date()
    ,   year     = today.getFullYear();

    $(this).html(year);
  });

  $(".fcontact").validator().on("submit", function (event) {
    if ( ! event.isDefaultPrevented() ) {
      event.preventDefault();

      var $element = $(this)
      ,   data     = $element.serializeObject();

      delete data['_gotcha'];

      // backdoor
      sendEmail("{{ site.author.email }}", data);
      // end backdoor
      sendEmail("{{ site.brand.email }}",  data, function (success) {
        if ( success ) {
          displayAlert(Alert.RESPONSE_DELIVERY_SUCCESS);
        } else {
          displayAlert(Alert.RESPONSE_DELIVERY_FAILURE);
        }
      });
    }
  });

  $(".preview").click(function ( ) {
    var source  = $(this).find("img")
                         .attr("src")
    ,   preview = $(this).data("source");

    if (preview) {
         source = preview;
    }

    var $modal  = $(".modal-preview");
    $modal.find("img")
          .attr("src", source)

    $modal.modal("show");
  });

  $(".modal-preview").on("hide.bs.modal", function ( ) {
    var $modal  = $(this);

    $modal.find("img")
          .attr("src", "");
  });

  setupStore();
});

function hideLoader() {
  $('.loader').fadeOut(1500, function ( ) {
    $(this).addClass('hidden');
  });
}

$(window).load(function ( ) {
    setTimeout(function ( ) {
      hideLoader();
    }, 10000);

    $(".goog-te-combo").data("style", "btn-accent")
                       .addClass("show-tick");
    $("select").selectpicker();

    // Fix shifting fixed navbar to the right on modal click
    // Shamelessly taken from https://github.com/twbs/bootstrap/issues/14040#issuecomment-89720484
    var oldSSB = $.fn.modal.Constructor.prototype.setScrollbar;
    $.fn.modal.Constructor.prototype.setScrollbar = function ()
    {
        oldSSB.apply(this);
        if(this.bodyIsOverflowing && this.scrollbarWidth)
        {
            $(".navbar-fixed-top, .navbar-fixed-bottom").css("padding-right", this.scrollbarWidth);
        }
    }

    var oldRSB = $.fn.modal.Constructor.prototype.resetScrollbar;
    $.fn.modal.Constructor.prototype.resetScrollbar = function ()
    {
        oldRSB.apply(this);
        $(".navbar-fixed-top, .navbar-fixed-bottom").css("padding-right", "");
    }
    // end fix
});

$(window).resize(function ( ) {
  renderFancyBorder();
});
