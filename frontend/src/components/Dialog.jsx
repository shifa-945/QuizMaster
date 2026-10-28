import { useEffect, useRef } from 'react';

const VARIANTS = {
  success: { icon: '✓', color: '#557a1f', background: '#f0f8e8' },
  warning: { icon: '!', color: '#8a6d00', background: '#fff8dc' },
  danger: { icon: '×', color: '#a33a2b', background: '#fdecea' },
  info: { icon: 'i', color: '#556b2f', background: '#f0f8e8' },
};

function Dialog({
  open,
  title,
  message,
  confirmLabel = 'OK',
  variant = 'info',
  onConfirm,
}) {
  const confirmRef = useRef(null);

  useEffect(() => {
    if (!open) return undefined;

    const handleKeyDown = (event) => {
      if (event.key === 'Escape') {
        event.preventDefault();
        onConfirm?.();
      }
    };

    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    document.addEventListener('keydown', handleKeyDown);
    confirmRef.current?.focus();

    return () => {
      document.body.style.overflow = previousOverflow;
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [open, onConfirm]);

  if (!open) return null;

  const palette = VARIANTS[variant] || VARIANTS.info;

  return (
    <div className="qm-dialog-overlay">
      <div
        className="qm-dialog"
        role="dialog"
        aria-modal="true"
        aria-labelledby="qm-dialog-title"
        aria-describedby="qm-dialog-message"
      >
        <div
          className="qm-dialog-icon"
          style={{ color: palette.color, background: palette.background }}
          aria-hidden="true"
        >
          {palette.icon}
        </div>

        <h2 id="qm-dialog-title" className="qm-dialog-title">{title}</h2>
        <p id="qm-dialog-message" className="qm-dialog-message">{message}</p>

        <button
          ref={confirmRef}
          type="button"
          className="qm-dialog-confirm"
          onClick={onConfirm}
        >
          {confirmLabel}
        </button>
      </div>
    </div>
  );
}

export default Dialog;
