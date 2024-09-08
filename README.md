# Django Signals Demo

This project demonstrates the behavior of Django signals in various scenarios, addressing key questions about their execution in the context of database transactions and threading.

## Project Structure

```
signalsdemo/
├── manage.py
├── signalsdemo/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── demoapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    ├── views.py
    └── management/
        └── commands/
            ├── test_signals.py
            ├── test_signal_thread.py
            └── test_signal_transaction.py
```

## Key Questions Addressed

### 1. Are Django signals executed synchronously or asynchronously?

Django signals are executed synchronously by default. This means that when a signal is triggered, the signal handler is executed immediately, blocking the main execution until it completes.

To demonstrate this, run:

```bash
python manage.py test_signals
```

You'll see that the total execution time is approximately the sum of the time taken by each signal handler, proving their synchronous nature.

### 2. Do Django signals run in the same thread as the caller?

Yes, Django signals run in the same thread as the caller by default. This means that signal handlers are executed in the main thread of your Django application.

To demonstrate this, run:

```bash
python manage.py test_signal_thread
```

You'll see that the thread ID and name are the same for both the main execution and the signal handlers.

### 3. Do Django signals run in the same database transaction as the caller?

Yes, Django signals run in the same database transaction as the caller by default. This means that any database operations performed in the signal handler are part of the same transaction as the operation that triggered the signal.

To demonstrate this, run:

```bash
python manage.py test_signal_transaction
```

You'll see that changes made in the signal handler are visible within the same transaction and are committed or rolled back along with the caller's changes.

## Conclusions

This project demonstrates that:

1. Django signals are synchronous by default.
2. They run in the same thread as the caller.
3. They operate within the same database transaction as the caller.

These characteristics are important to consider when designing systems that rely on Django signals, especially in scenarios involving database transactions or where thread safety is a concern.
