/**  @odoo-module **/

import {NavBar} from "@web/webclient/navbar/navbar";
import {patch} from "@web/core/utils/patch";



patch(NavBar.prototype, {
    setup() {
        super.setup(...arguments);

        // Ikonalarni dinamik sozlash
        this.updateIcons = () => {
            document.querySelectorAll('.o_custom_navbar_menu .nav-item').forEach(item => {
                const iconImg = item.querySelector('img.o_nav_items_icon');
                if (iconImg) {
                    const iconData = item.getAttribute('data-icon-data');
                    const iconMimeType = item.getAttribute('data-icon-mimetype');
                    if (iconData) {
                        iconImg.src = 'data:' + iconMimeType + ';base64,' + iconData;
                    }
                }
            });
        };

        // Dinamik ikonkalarni yangilash
        this.updateIcons();
    }
    

})

NavBar.template = "new_module.NavBar"