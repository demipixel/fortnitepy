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

  $('.source-link').parent().click(function(event) {
    event.preventDefault();

    const rawFullname = $(this).attr('class').split(/\s+/).find(function (c) {
      return c.startsWith('fullname')
    });
    if (!rawFullname) return;

    const split = rawFullname.split('-');
    const fullname = split.slice(1, split.length).join('.');

    window.location.href = $(this).attr('href') + '?referrer=' + fullname;
  });
});
