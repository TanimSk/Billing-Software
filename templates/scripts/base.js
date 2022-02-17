
let restore_state = true;

function window_control(action) {
    if (action == 'rmax') {
        if (restore_state) {
            pywebview.api.window_control("maximize", window.screen.width, window.screen.height);
            restore_state = false;
        }
        else {
            pywebview.api.window_control("restore", window.screen.width, window.screen.height)
            restore_state = true;
        }
    }
    else {
        pywebview.api.window_control(action, 0, 0);
    }
}