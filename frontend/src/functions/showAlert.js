export function modalAlert(modalStore, message, title) {
    const alertModal = {
        type: 'alert',
        title: title ?? 'Alert',
        body: message ?? 'Message',
    };
    modalStore.trigger(alertModal);
}
