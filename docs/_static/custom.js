$(document).ready(function () {
  var sections = $('div.section');
  var activeLink = null;
  var bottomHeightThreshold = $(document).height() - 30;

  $(window).scroll(function (event) {
    var distanceFromTop = $(this).scrollTop();
    var currentSection = null;

    if(distanceFromTop + window.innerHeight > bottomHeightThreshold) {
      currentSection = $(sections[sections.length - 1]);
    }
    else {
      sections.each(function () {
        var section = $(this);
        if (section.offset().top - 1 < distanceFromTop) {
          currentSection = section;
        }
      });
    }

    if (activeLink) {
      activeLink.parent().removeClass('active');
    }

    if (currentSection) {
      activeLink = $('.sphinxsidebar a[href="#' + currentSection.attr('id') + '"]');
      activeLink.parent().addClass('active');
    }
  });

  $('.source-link').parent().click(function() {
    const rawFullname = $(this).attr('class').split(/\s+/).find(function (c) {
      return c.startsWith('fullname')
    });
    if (!rawFullname) return;

    const split = rawFullname.split('-');
    const fullname = split.slice(1, split.length).join('.');

    if (fullname === 'none') fullname = null;
    sessionStorage.setItem('referrer', fullname);
  });

  $('.docs-link').click(function(event) {
    const fullname = sessionStorage.getItem('referrer');
    if (!fullname) return;

    const elem = $(this);
    const newHref = elem.attr('href').split('#').slice(0, 1) + '#' + fullname;
    
    event.preventDefault();
    console.log(newHref);
    // window.location.href = newHref;
  });
});
