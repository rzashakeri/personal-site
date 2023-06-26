/**
 * Codex: jQuery Plugin for sodomizing texts for a given time.
 *
 * @author: @minimo-labs
 * @version: 1.1.4
 * @url: https://github.com/minimo-io/jquery-codex
 *
 */

;(function($) {

    $.codex = function(element, options) {

        var plugin = this;
        plugin.settings = {};

        var $element = $(element),
        element = element;


        var defaults = {
            effect : "allofasudden", // charbychar || allofasudden || typewriter
            keep_whitespaces : true, // wheter keep whitespaces or fill them also with a random char
            speed : 100, // speed in which random chars will appear in letters not yet revelaed
            duration : 3000, // in some effects you can specify the total duration in other it is auto calculated
            final_text: $element.text(),
            reveal: 1000, // in char by char effect, this is the number of miliseconds that will take for char reveal
            total_iterations : 0,
            interval : -1
        }




        plugin.init = function() {

            plugin.settings = $.extend({}, defaults, options);

            var el = $element;
            var str = el.text();



            if (
              plugin.settings.effect == "charbychar"
            || plugin.settings.effect == "typewriter"
            ) {
              var pos_limit = 0; // only randomize text from here to the end
              var pos_total = str.length;
              var internal_char_reveal_counter = 0;
              plugin.settings.duration = pos_total * plugin.settings.reveal; // duration is auto calculated with the reveal value

              plugin.settings.interval = setInterval( function(){

                  // char changer effect
                  el.text( sodomizer_char_by_char( str, pos_limit,  plugin.settings.effect) );

                  // time controller
                  plugin.settings.total_iterations += plugin.settings.speed;
                  internal_char_reveal_counter += plugin.settings.speed;

                  // reset to wait for the next reveal and fix the character limit
                  if (internal_char_reveal_counter >= plugin.settings.reveal){
                    internal_char_reveal_counter = 0;
                    pos_limit++;
                  }
                  // end and stop interval
                  if ( plugin.settings.total_iterations >= plugin.settings.duration ) {
                      clearInterval(plugin.settings.interval);
                      plugin.settings.total_iterations = 0;
                      plugin.settings.interval = -1;
                      // el.text(plugin.settings.final_text);
                      el.text(str);
                  }


              }, plugin.settings.speed );



            }

            if ( plugin.settings.effect == "allofasudden"){

              plugin.settings.interval = setInterval( function(){

                  // char changer effect
                  el.text( sodomizer_change_each_position( str ) );

                  // time controller
                  plugin.settings.total_iterations += plugin.settings.speed;
                  // end and stop interval
                  if ( plugin.settings.total_iterations >= plugin.settings.duration ) {
                      clearInterval(plugin.settings.interval);
                      plugin.settings.total_iterations = 0;
                      plugin.settings.interval = -1;
                      el.text(plugin.settings.final_text);
                  }


              }, plugin.settings.speed );

            }


        }




        /**
         * get a raondom char between two limits
         */
        var codex_get_random_char = function (max, min){
            // 33 - 126 ascii (decimal)
            var random = Math.floor(Math.random() * (max - min + 1) + min);
            return String.fromCharCode(random);

        }

        /**
         * main sodomizer method
         */
        var sodomizer_change_each_position = function (s){
            var ret_string = "";
            for (var c = 0; c < s.length; c++){
              if ( s.charCodeAt(c) == 32 && plugin.settings.keep_whitespaces ){
                ret_string += " ";
              }else{
                ret_string += codex_get_random_char(33, 126);
              }
            }
            return ret_string;
        }
        /**
         * change the original revealing characters one by one
         */
        var sodomizer_char_by_char = function(s, poslimit, effect){
          var ret_string = "";
          var fixed_chars = s.substr(0, poslimit);

          for (var c = poslimit; c < s.length; c++){
              if ( s.charCodeAt(c) == 32 && plugin.settings.keep_whitespaces ){
                ret_string += " ";
              }else{
                ret_string += codex_get_random_char(33, 126);
              }
          }
          if (effect == "typewriter") ret_string = "|";
          return fixed_chars + ret_string;
        }


        plugin.init();

    }

    $.fn.codex = function(options) {

        return this.each(function() {

            var plugin = new $.codex(this, options);
            $(this).data('codex', plugin);

        });

    }

})(jQuery);
