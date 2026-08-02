N:\Ai\dropservice-agent>tree /f
Folder PATH listing
Volume serial number is 903B-113A
N:.
│   input.txt
│   PROJECT_MEMORY.md
│   test.py
│
├───app
│   │   .gitignore
│   │   agencyos.db
│   │   git
│   │
│   ├───docs
│   │       ARCHITECTURE.md
│   │       PROJECT_MEMORY.md
│   │       ROADMAP.md
│   │
│   ├───legacy
│   │       agent.py
│   │       extractor.py
│   │       formatter.py
│   │       lead_manager.py
│   │       prompts.py
│   │       reviewer.py
│   │       test_extract.py
│   │       test_lead.py
│   │
│   ├───src
│   │   │   main.py
│   │   │
│   │   ├───agents
│   │   │   │   lead_intake.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           lead_intake.cpython-314.pyc
│   │   │           __init__.cpython-314.pyc
│   │   │
│   │   ├───api
│   │   │   │   main.py
│   │   │   │   schemas.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           main.cpython-314.pyc
│   │   │           schemas.cpython-314.pyc
│   │   │           __init__.cpython-314.pyc
│   │   │
│   │   ├───config
│   │   │   │   prompts.py
│   │   │   │   settings.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           prompts.cpython-314.pyc
│   │   │           settings.cpython-314.pyc
│   │   │           __init__.cpython-314.pyc
│   │   │
│   │   ├───domain
│   │   │   │   lead.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           lead.cpython-314.pyc
│   │   │           __init__.cpython-314.pyc
│   │   │
│   │   ├───memory
│   │   ├───services
│   │   │   │   lead_service.py
│   │   │   │   lead_state_service.py
│   │   │   │   llm_service.py
│   │   │   │   llm_test.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           lead_state_service.cpython-314.pyc
│   │   │           llm_service.cpython-314.pyc
│   │   │           llm_test.cpython-314.pyc
│   │   │           __init__.cpython-314.pyc
│   │   │
│   │   ├───skills
│   │   │   │   lead_analysis.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           lead_analysis.cpython-314.pyc
│   │   │
│   │   ├───storage
│   │   │   │   database.py
│   │   │   │   lead_repository.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           database.cpython-314.pyc
│   │   │           lead_repository.cpython-314.pyc
│   │   │           __init__.cpython-314.pyc
│   │   │
│   │   ├───tools
│   │   │       __init__.py
│   │   │
│   │   ├───workflows
│   │   │   │   lead_workflow.py
│   │   │   │   __init__.py
│   │   │   │
│   │   │   └───__pycache__
│   │   │           lead_workflow.cpython-314.pyc
│   │   │           __init__.cpython-314.pyc
│   │   │
│   │   └───__pycache__
│   │           main.cpython-314.pyc
│   │
│   ├───tests
│   └───__pycache__
│           extractor.cpython-314.pyc
│           formatter.cpython-314.pyc
│           lead_manager.cpython-314.pyc
│           prompts.cpython-314.pyc
│           reviewer.cpython-314.pyc
│
├───database
│       customers.json
│       leads.json
│
├───outputs
│       result_20260725_152724.txt
│       result_20260725_153139.txt
│       result_20260725_153526.txt
│       result_20260725_154042.txt
│       result_20260725_155045.txt
│       result_20260725_155721.txt
│       result_20260725_155852.txt
│       result_20260725_160405.txt
│       result_20260725_160908.txt
│       result_20260725_161723.txt
│       result_20260725_162639.txt
│       result_20260725_163316.txt
│       result_20260725_164453.txt
│       result_20260725_165036.txt
│       result_20260725_165329.txt
│       result_20260728_041926.txt
│       result_20260728_044614.txt
│
└───venv
    │   .gitignore
    │   pyvenv.cfg
    │
    ├───Include
    ├───Lib
    │   └───site-packages
    │       │   ada92cb5d92a588d1b93__mypyc.cp314-win_amd64.pyd
    │       │   typing_extensions.py
    │       │
    │       ├───annotated_types
    │       │   │   py.typed
    │       │   │   test_cases.py
    │       │   │   __init__.py
    │       │   │
    │       │   └───__pycache__
    │       │           test_cases.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───annotated_types-0.8.0.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───anyio
    │       │   │   from_thread.py
    │       │   │   functools.py
    │       │   │   itertools.py
    │       │   │   lowlevel.py
    │       │   │   py.typed
    │       │   │   pytest_plugin.py
    │       │   │   to_interpreter.py
    │       │   │   to_process.py
    │       │   │   to_thread.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───abc
    │       │   │   │   _eventloop.py
    │       │   │   │   _resources.py
    │       │   │   │   _sockets.py
    │       │   │   │   _streams.py
    │       │   │   │   _subprocesses.py
    │       │   │   │   _tasks.py
    │       │   │   │   _testing.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           _eventloop.cpython-314.pyc
    │       │   │           _resources.cpython-314.pyc
    │       │   │           _sockets.cpython-314.pyc
    │       │   │           _streams.cpython-314.pyc
    │       │   │           _subprocesses.cpython-314.pyc
    │       │   │           _tasks.cpython-314.pyc
    │       │   │           _testing.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───streams
    │       │   │   │   buffered.py
    │       │   │   │   file.py
    │       │   │   │   memory.py
    │       │   │   │   stapled.py
    │       │   │   │   text.py
    │       │   │   │   tls.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           buffered.cpython-314.pyc
    │       │   │           file.cpython-314.pyc
    │       │   │           memory.cpython-314.pyc
    │       │   │           stapled.cpython-314.pyc
    │       │   │           text.cpython-314.pyc
    │       │   │           tls.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_backends
    │       │   │   │   _asyncio.py
    │       │   │   │   _trio.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           _asyncio.cpython-314.pyc
    │       │   │           _trio.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_core
    │       │   │   │   _asyncio_selector_thread.py
    │       │   │   │   _contextmanagers.py
    │       │   │   │   _eventloop.py
    │       │   │   │   _exceptions.py
    │       │   │   │   _fileio.py
    │       │   │   │   _resources.py
    │       │   │   │   _signals.py
    │       │   │   │   _sockets.py
    │       │   │   │   _streams.py
    │       │   │   │   _subprocesses.py
    │       │   │   │   _synchronization.py
    │       │   │   │   _tasks.py
    │       │   │   │   _tempfile.py
    │       │   │   │   _testing.py
    │       │   │   │   _typedattr.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           _asyncio_selector_thread.cpython-314.pyc
    │       │   │           _contextmanagers.cpython-314.pyc
    │       │   │           _eventloop.cpython-314.pyc
    │       │   │           _exceptions.cpython-314.pyc
    │       │   │           _fileio.cpython-314.pyc
    │       │   │           _resources.cpython-314.pyc
    │       │   │           _signals.cpython-314.pyc
    │       │   │           _sockets.cpython-314.pyc
    │       │   │           _streams.cpython-314.pyc
    │       │   │           _subprocesses.cpython-314.pyc
    │       │   │           _synchronization.cpython-314.pyc
    │       │   │           _tasks.cpython-314.pyc
    │       │   │           _tempfile.cpython-314.pyc
    │       │   │           _testing.cpython-314.pyc
    │       │   │           _typedattr.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           from_thread.cpython-314.pyc
    │       │           functools.cpython-314.pyc
    │       │           itertools.cpython-314.pyc
    │       │           lowlevel.cpython-314.pyc
    │       │           pytest_plugin.cpython-314.pyc
    │       │           to_interpreter.cpython-314.pyc
    │       │           to_process.cpython-314.pyc
    │       │           to_thread.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───anyio-4.14.2.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   scm_file_list.json
    │       │   │   scm_version.json
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───certifi
    │       │   │   cacert.pem
    │       │   │   core.py
    │       │   │   py.typed
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │
    │       │   ├───tests
    │       │   │   │   test_certify.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           test_certify.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           core.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │
    │       ├───certifi-2026.7.22.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───charset_normalizer
    │       │   │   api.py
    │       │   │   cd.cp314-win_amd64.pyd
    │       │   │   cd.py
    │       │   │   constant.py
    │       │   │   legacy.py
    │       │   │   md.cp314-win_amd64.pyd
    │       │   │   md.py
    │       │   │   models.py
    │       │   │   py.typed
    │       │   │   utils.py
    │       │   │   version.py
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │
    │       │   ├───cli
    │       │   │   │   __init__.py
    │       │   │   │   __main__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           __init__.cpython-314.pyc
    │       │   │           __main__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           api.cpython-314.pyc
    │       │           cd.cpython-314.pyc
    │       │           constant.cpython-314.pyc
    │       │           legacy.cpython-314.pyc
    │       │           md.cpython-314.pyc
    │       │           models.cpython-314.pyc
    │       │           utils.cpython-314.pyc
    │       │           version.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │
    │       ├───charset_normalizer-3.4.9.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───colorama
    │       │   │   ansi.py
    │       │   │   ansitowin32.py
    │       │   │   initialise.py
    │       │   │   win32.py
    │       │   │   winterm.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───tests
    │       │   │   │   ansitowin32_test.py
    │       │   │   │   ansi_test.py
    │       │   │   │   initialise_test.py
    │       │   │   │   isatty_test.py
    │       │   │   │   utils.py
    │       │   │   │   winterm_test.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           ansitowin32_test.cpython-314.pyc
    │       │   │           ansi_test.cpython-314.pyc
    │       │   │           initialise_test.cpython-314.pyc
    │       │   │           isatty_test.cpython-314.pyc
    │       │   │           utils.cpython-314.pyc
    │       │   │           winterm_test.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           ansi.cpython-314.pyc
    │       │           ansitowin32.cpython-314.pyc
    │       │           initialise.cpython-314.pyc
    │       │           win32.cpython-314.pyc
    │       │           winterm.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───colorama-0.4.6.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE.txt
    │       │
    │       ├───distro
    │       │   │   distro.py
    │       │   │   py.typed
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │
    │       │   └───__pycache__
    │       │           distro.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │
    │       ├───distro-1.9.0.dist-info
    │       │       entry_points.txt
    │       │       INSTALLER
    │       │       LICENSE
    │       │       METADATA
    │       │       RECORD
    │       │       top_level.txt
    │       │       WHEEL
    │       │
    │       ├───h11
    │       │   │   py.typed
    │       │   │   _abnf.py
    │       │   │   _connection.py
    │       │   │   _events.py
    │       │   │   _headers.py
    │       │   │   _readers.py
    │       │   │   _receivebuffer.py
    │       │   │   _state.py
    │       │   │   _util.py
    │       │   │   _version.py
    │       │   │   _writers.py
    │       │   │   __init__.py
    │       │   │
    │       │   └───__pycache__
    │       │           _abnf.cpython-314.pyc
    │       │           _connection.cpython-314.pyc
    │       │           _events.cpython-314.pyc
    │       │           _headers.cpython-314.pyc
    │       │           _readers.cpython-314.pyc
    │       │           _receivebuffer.cpython-314.pyc
    │       │           _state.cpython-314.pyc
    │       │           _util.cpython-314.pyc
    │       │           _version.cpython-314.pyc
    │       │           _writers.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───h11-0.16.0.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE.txt
    │       │
    │       ├───httpcore
    │       │   │   py.typed
    │       │   │   _api.py
    │       │   │   _exceptions.py
    │       │   │   _models.py
    │       │   │   _ssl.py
    │       │   │   _synchronization.py
    │       │   │   _trace.py
    │       │   │   _utils.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───_async
    │       │   │   │   connection.py
    │       │   │   │   connection_pool.py
    │       │   │   │   http11.py
    │       │   │   │   http2.py
    │       │   │   │   http_proxy.py
    │       │   │   │   interfaces.py
    │       │   │   │   socks_proxy.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           connection.cpython-314.pyc
    │       │   │           connection_pool.cpython-314.pyc
    │       │   │           http11.cpython-314.pyc
    │       │   │           http2.cpython-314.pyc
    │       │   │           http_proxy.cpython-314.pyc
    │       │   │           interfaces.cpython-314.pyc
    │       │   │           socks_proxy.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_backends
    │       │   │   │   anyio.py
    │       │   │   │   auto.py
    │       │   │   │   base.py
    │       │   │   │   mock.py
    │       │   │   │   sync.py
    │       │   │   │   trio.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           anyio.cpython-314.pyc
    │       │   │           auto.cpython-314.pyc
    │       │   │           base.cpython-314.pyc
    │       │   │           mock.cpython-314.pyc
    │       │   │           sync.cpython-314.pyc
    │       │   │           trio.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_sync
    │       │   │   │   connection.py
    │       │   │   │   connection_pool.py
    │       │   │   │   http11.py
    │       │   │   │   http2.py
    │       │   │   │   http_proxy.py
    │       │   │   │   interfaces.py
    │       │   │   │   socks_proxy.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           connection.cpython-314.pyc
    │       │   │           connection_pool.cpython-314.pyc
    │       │   │           http11.cpython-314.pyc
    │       │   │           http2.cpython-314.pyc
    │       │   │           http_proxy.cpython-314.pyc
    │       │   │           interfaces.cpython-314.pyc
    │       │   │           socks_proxy.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           _api.cpython-314.pyc
    │       │           _exceptions.cpython-314.pyc
    │       │           _models.cpython-314.pyc
    │       │           _ssl.cpython-314.pyc
    │       │           _synchronization.cpython-314.pyc
    │       │           _trace.cpython-314.pyc
    │       │           _utils.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───httpcore-1.0.9.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE.md
    │       │
    │       ├───httpx
    │       │   │   py.typed
    │       │   │   _api.py
    │       │   │   _auth.py
    │       │   │   _client.py
    │       │   │   _config.py
    │       │   │   _content.py
    │       │   │   _decoders.py
    │       │   │   _exceptions.py
    │       │   │   _main.py
    │       │   │   _models.py
    │       │   │   _multipart.py
    │       │   │   _status_codes.py
    │       │   │   _types.py
    │       │   │   _urlparse.py
    │       │   │   _urls.py
    │       │   │   _utils.py
    │       │   │   __init__.py
    │       │   │   __version__.py
    │       │   │
    │       │   ├───_transports
    │       │   │   │   asgi.py
    │       │   │   │   base.py
    │       │   │   │   default.py
    │       │   │   │   mock.py
    │       │   │   │   wsgi.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           asgi.cpython-314.pyc
    │       │   │           base.cpython-314.pyc
    │       │   │           default.cpython-314.pyc
    │       │   │           mock.cpython-314.pyc
    │       │   │           wsgi.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           _api.cpython-314.pyc
    │       │           _auth.cpython-314.pyc
    │       │           _client.cpython-314.pyc
    │       │           _config.cpython-314.pyc
    │       │           _content.cpython-314.pyc
    │       │           _decoders.cpython-314.pyc
    │       │           _exceptions.cpython-314.pyc
    │       │           _main.cpython-314.pyc
    │       │           _models.cpython-314.pyc
    │       │           _multipart.cpython-314.pyc
    │       │           _status_codes.cpython-314.pyc
    │       │           _types.cpython-314.pyc
    │       │           _urlparse.cpython-314.pyc
    │       │           _urls.cpython-314.pyc
    │       │           _utils.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │           __version__.cpython-314.pyc
    │       │
    │       ├───httpx-0.28.1.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE.md
    │       │
    │       ├───idna
    │       │   │   cli.py
    │       │   │   codec.py
    │       │   │   compat.py
    │       │   │   core.py
    │       │   │   idnadata.py
    │       │   │   intranges.py
    │       │   │   package_data.py
    │       │   │   py.typed
    │       │   │   uts46data.py
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │
    │       │   └───__pycache__
    │       │           cli.cpython-314.pyc
    │       │           codec.cpython-314.pyc
    │       │           compat.cpython-314.pyc
    │       │           core.cpython-314.pyc
    │       │           idnadata.cpython-314.pyc
    │       │           intranges.cpython-314.pyc
    │       │           package_data.cpython-314.pyc
    │       │           uts46data.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │
    │       ├───idna-3.18.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE.md
    │       │
    │       ├───images
    │       │       logo.gif
    │       │       tqdm.gif
    │       │
    │       ├───jiter
    │       │   │   jiter.cp314-win_amd64.pyd
    │       │   │   py.typed
    │       │   │   __init__.py
    │       │   │   __init__.pyi
    │       │   │
    │       │   └───__pycache__
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───jiter-0.16.0.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   ├───licenses
    │       │   │       LICENSE
    │       │   │
    │       │   └───sboms
    │       │           jiter-python.cyclonedx.json
    │       │
    │       ├───openai
    │       │   │   pagination.py
    │       │   │   py.typed
    │       │   │   version.py
    │       │   │   _base_client.py
    │       │   │   _client.py
    │       │   │   _compat.py
    │       │   │   _constants.py
    │       │   │   _event_handler.py
    │       │   │   _exceptions.py
    │       │   │   _files.py
    │       │   │   _httpx2.py
    │       │   │   _legacy_response.py
    │       │   │   _models.py
    │       │   │   _module_client.py
    │       │   │   _provider.py
    │       │   │   _qs.py
    │       │   │   _resource.py
    │       │   │   _response.py
    │       │   │   _send_queue.py
    │       │   │   _streaming.py
    │       │   │   _types.py
    │       │   │   _version.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───auth
    │       │   │   │   _workload.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           _workload.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───helpers
    │       │   │   │   local_audio_player.py
    │       │   │   │   microphone.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           local_audio_player.cpython-314.pyc
    │       │   │           microphone.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───lib
    │       │   │   │   .keep
    │       │   │   │   azure.py
    │       │   │   │   bedrock.py
    │       │   │   │   _bedrock_auth.py
    │       │   │   │   _old_api.py
    │       │   │   │   _pydantic.py
    │       │   │   │   _realtime.py
    │       │   │   │   _tools.py
    │       │   │   │   _validators.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   ├───streaming
    │       │   │   │   │   _assistants.py
    │       │   │   │   │   _deltas.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───chat
    │       │   │   │   │   │   _completions.py
    │       │   │   │   │   │   _events.py
    │       │   │   │   │   │   _types.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _completions.cpython-314.pyc
    │       │   │   │   │           _events.cpython-314.pyc
    │       │   │   │   │           _types.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───responses
    │       │   │   │   │   │   _events.py
    │       │   │   │   │   │   _responses.py
    │       │   │   │   │   │   _types.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _events.cpython-314.pyc
    │       │   │   │   │           _responses.cpython-314.pyc
    │       │   │   │   │           _types.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _assistants.cpython-314.pyc
    │       │   │   │           _deltas.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───_parsing
    │       │   │   │   │   _completions.py
    │       │   │   │   │   _responses.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _completions.cpython-314.pyc
    │       │   │   │           _responses.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           azure.cpython-314.pyc
    │       │   │           bedrock.cpython-314.pyc
    │       │   │           _bedrock_auth.cpython-314.pyc
    │       │   │           _old_api.cpython-314.pyc
    │       │   │           _pydantic.cpython-314.pyc
    │       │   │           _realtime.cpython-314.pyc
    │       │   │           _tools.cpython-314.pyc
    │       │   │           _validators.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───providers
    │       │   │   │   bedrock.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           bedrock.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───resources
    │       │   │   │   batches.py
    │       │   │   │   completions.py
    │       │   │   │   embeddings.py
    │       │   │   │   files.py
    │       │   │   │   images.py
    │       │   │   │   models.py
    │       │   │   │   moderations.py
    │       │   │   │   videos.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   ├───admin
    │       │   │   │   │   admin.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───organization
    │       │   │   │   │   │   admin_api_keys.py
    │       │   │   │   │   │   audit_logs.py
    │       │   │   │   │   │   certificates.py
    │       │   │   │   │   │   data_retention.py
    │       │   │   │   │   │   invites.py
    │       │   │   │   │   │   organization.py
    │       │   │   │   │   │   roles.py
    │       │   │   │   │   │   spend_alerts.py
    │       │   │   │   │   │   spend_limit.py
    │       │   │   │   │   │   usage.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   ├───groups
    │       │   │   │   │   │   │   groups.py
    │       │   │   │   │   │   │   roles.py
    │       │   │   │   │   │   │   users.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           groups.cpython-314.pyc
    │       │   │   │   │   │           roles.cpython-314.pyc
    │       │   │   │   │   │           users.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   ├───projects
    │       │   │   │   │   │   │   api_keys.py
    │       │   │   │   │   │   │   certificates.py
    │       │   │   │   │   │   │   data_retention.py
    │       │   │   │   │   │   │   hosted_tool_permissions.py
    │       │   │   │   │   │   │   model_permissions.py
    │       │   │   │   │   │   │   projects.py
    │       │   │   │   │   │   │   rate_limits.py
    │       │   │   │   │   │   │   roles.py
    │       │   │   │   │   │   │   spend_alerts.py
    │       │   │   │   │   │   │   spend_limit.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   ├───groups
    │       │   │   │   │   │   │   │   groups.py
    │       │   │   │   │   │   │   │   roles.py
    │       │   │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │   │
    │       │   │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │   │           groups.cpython-314.pyc
    │       │   │   │   │   │   │           roles.cpython-314.pyc
    │       │   │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │   │
    │       │   │   │   │   │   ├───service_accounts
    │       │   │   │   │   │   │   │   api_keys.py
    │       │   │   │   │   │   │   │   service_accounts.py
    │       │   │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │   │
    │       │   │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │   │           api_keys.cpython-314.pyc
    │       │   │   │   │   │   │           service_accounts.cpython-314.pyc
    │       │   │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │   │
    │       │   │   │   │   │   ├───users
    │       │   │   │   │   │   │   │   roles.py
    │       │   │   │   │   │   │   │   users.py
    │       │   │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │   │
    │       │   │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │   │           roles.cpython-314.pyc
    │       │   │   │   │   │   │           users.cpython-314.pyc
    │       │   │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           api_keys.cpython-314.pyc
    │       │   │   │   │   │           certificates.cpython-314.pyc
    │       │   │   │   │   │           data_retention.cpython-314.pyc
    │       │   │   │   │   │           hosted_tool_permissions.cpython-314.pyc
    │       │   │   │   │   │           model_permissions.cpython-314.pyc
    │       │   │   │   │   │           projects.cpython-314.pyc
    │       │   │   │   │   │           rate_limits.cpython-314.pyc
    │       │   │   │   │   │           roles.cpython-314.pyc
    │       │   │   │   │   │           spend_alerts.cpython-314.pyc
    │       │   │   │   │   │           spend_limit.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   ├───users
    │       │   │   │   │   │   │   roles.py
    │       │   │   │   │   │   │   users.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           roles.cpython-314.pyc
    │       │   │   │   │   │           users.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           admin_api_keys.cpython-314.pyc
    │       │   │   │   │           audit_logs.cpython-314.pyc
    │       │   │   │   │           certificates.cpython-314.pyc
    │       │   │   │   │           data_retention.cpython-314.pyc
    │       │   │   │   │           invites.cpython-314.pyc
    │       │   │   │   │           organization.cpython-314.pyc
    │       │   │   │   │           roles.cpython-314.pyc
    │       │   │   │   │           spend_alerts.cpython-314.pyc
    │       │   │   │   │           spend_limit.cpython-314.pyc
    │       │   │   │   │           usage.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           admin.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───audio
    │       │   │   │   │   audio.py
    │       │   │   │   │   speech.py
    │       │   │   │   │   transcriptions.py
    │       │   │   │   │   translations.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           audio.cpython-314.pyc
    │       │   │   │           speech.cpython-314.pyc
    │       │   │   │           transcriptions.cpython-314.pyc
    │       │   │   │           translations.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───beta
    │       │   │   │   │   assistants.py
    │       │   │   │   │   beta.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───chatkit
    │       │   │   │   │   │   chatkit.py
    │       │   │   │   │   │   sessions.py
    │       │   │   │   │   │   threads.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           chatkit.cpython-314.pyc
    │       │   │   │   │           sessions.cpython-314.pyc
    │       │   │   │   │           threads.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───realtime
    │       │   │   │   │   │   realtime.py
    │       │   │   │   │   │   sessions.py
    │       │   │   │   │   │   transcription_sessions.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           realtime.cpython-314.pyc
    │       │   │   │   │           sessions.cpython-314.pyc
    │       │   │   │   │           transcription_sessions.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───responses
    │       │   │   │   │   │   input_items.py
    │       │   │   │   │   │   input_tokens.py
    │       │   │   │   │   │   responses.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           input_items.cpython-314.pyc
    │       │   │   │   │           input_tokens.cpython-314.pyc
    │       │   │   │   │           responses.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───threads
    │       │   │   │   │   │   messages.py
    │       │   │   │   │   │   threads.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   ├───runs
    │       │   │   │   │   │   │   runs.py
    │       │   │   │   │   │   │   steps.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           runs.cpython-314.pyc
    │       │   │   │   │   │           steps.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           messages.cpython-314.pyc
    │       │   │   │   │           threads.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           assistants.cpython-314.pyc
    │       │   │   │           beta.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───chat
    │       │   │   │   │   chat.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───completions
    │       │   │   │   │   │   completions.py
    │       │   │   │   │   │   messages.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           completions.cpython-314.pyc
    │       │   │   │   │           messages.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           chat.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───containers
    │       │   │   │   │   containers.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───files
    │       │   │   │   │   │   content.py
    │       │   │   │   │   │   files.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           content.cpython-314.pyc
    │       │   │   │   │           files.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           containers.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───conversations
    │       │   │   │   │   api.md
    │       │   │   │   │   conversations.py
    │       │   │   │   │   items.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           conversations.cpython-314.pyc
    │       │   │   │           items.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───evals
    │       │   │   │   │   evals.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───runs
    │       │   │   │   │   │   output_items.py
    │       │   │   │   │   │   runs.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           output_items.cpython-314.pyc
    │       │   │   │   │           runs.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           evals.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───fine_tuning
    │       │   │   │   │   fine_tuning.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───alpha
    │       │   │   │   │   │   alpha.py
    │       │   │   │   │   │   graders.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           alpha.cpython-314.pyc
    │       │   │   │   │           graders.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───checkpoints
    │       │   │   │   │   │   checkpoints.py
    │       │   │   │   │   │   permissions.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           checkpoints.cpython-314.pyc
    │       │   │   │   │           permissions.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───jobs
    │       │   │   │   │   │   checkpoints.py
    │       │   │   │   │   │   jobs.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           checkpoints.cpython-314.pyc
    │       │   │   │   │           jobs.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           fine_tuning.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───realtime
    │       │   │   │   │   api.md
    │       │   │   │   │   calls.py
    │       │   │   │   │   client_secrets.py
    │       │   │   │   │   realtime.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           calls.cpython-314.pyc
    │       │   │   │           client_secrets.cpython-314.pyc
    │       │   │   │           realtime.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───responses
    │       │   │   │   │   api.md
    │       │   │   │   │   input_items.py
    │       │   │   │   │   input_tokens.py
    │       │   │   │   │   responses.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           input_items.cpython-314.pyc
    │       │   │   │           input_tokens.cpython-314.pyc
    │       │   │   │           responses.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───skills
    │       │   │   │   │   content.py
    │       │   │   │   │   skills.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───versions
    │       │   │   │   │   │   content.py
    │       │   │   │   │   │   versions.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           content.cpython-314.pyc
    │       │   │   │   │           versions.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           content.cpython-314.pyc
    │       │   │   │           skills.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───uploads
    │       │   │   │   │   parts.py
    │       │   │   │   │   uploads.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           parts.cpython-314.pyc
    │       │   │   │           uploads.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───vector_stores
    │       │   │   │   │   files.py
    │       │   │   │   │   file_batches.py
    │       │   │   │   │   vector_stores.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           files.cpython-314.pyc
    │       │   │   │           file_batches.cpython-314.pyc
    │       │   │   │           vector_stores.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───webhooks
    │       │   │   │   │   api.md
    │       │   │   │   │   webhooks.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           webhooks.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           batches.cpython-314.pyc
    │       │   │           completions.cpython-314.pyc
    │       │   │           embeddings.cpython-314.pyc
    │       │   │           files.cpython-314.pyc
    │       │   │           images.cpython-314.pyc
    │       │   │           models.cpython-314.pyc
    │       │   │           moderations.cpython-314.pyc
    │       │   │           videos.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───types
    │       │   │   │   audio_model.py
    │       │   │   │   audio_response_format.py
    │       │   │   │   auto_file_chunking_strategy_param.py
    │       │   │   │   batch.py
    │       │   │   │   batch_create_params.py
    │       │   │   │   batch_error.py
    │       │   │   │   batch_list_params.py
    │       │   │   │   batch_request_counts.py
    │       │   │   │   batch_usage.py
    │       │   │   │   chat_model.py
    │       │   │   │   completion.py
    │       │   │   │   completion_choice.py
    │       │   │   │   completion_create_params.py
    │       │   │   │   completion_usage.py
    │       │   │   │   container_create_params.py
    │       │   │   │   container_create_response.py
    │       │   │   │   container_list_params.py
    │       │   │   │   container_list_response.py
    │       │   │   │   container_retrieve_response.py
    │       │   │   │   create_embedding_response.py
    │       │   │   │   deleted_skill.py
    │       │   │   │   embedding.py
    │       │   │   │   embedding_create_params.py
    │       │   │   │   embedding_model.py
    │       │   │   │   eval_create_params.py
    │       │   │   │   eval_create_response.py
    │       │   │   │   eval_custom_data_source_config.py
    │       │   │   │   eval_delete_response.py
    │       │   │   │   eval_list_params.py
    │       │   │   │   eval_list_response.py
    │       │   │   │   eval_retrieve_response.py
    │       │   │   │   eval_stored_completions_data_source_config.py
    │       │   │   │   eval_update_params.py
    │       │   │   │   eval_update_response.py
    │       │   │   │   file_chunking_strategy.py
    │       │   │   │   file_chunking_strategy_param.py
    │       │   │   │   file_content.py
    │       │   │   │   file_create_params.py
    │       │   │   │   file_deleted.py
    │       │   │   │   file_list_params.py
    │       │   │   │   file_object.py
    │       │   │   │   file_purpose.py
    │       │   │   │   image.py
    │       │   │   │   images_response.py
    │       │   │   │   image_create_variation_params.py
    │       │   │   │   image_edit_completed_event.py
    │       │   │   │   image_edit_params.py
    │       │   │   │   image_edit_partial_image_event.py
    │       │   │   │   image_edit_stream_event.py
    │       │   │   │   image_generate_params.py
    │       │   │   │   image_gen_completed_event.py
    │       │   │   │   image_gen_partial_image_event.py
    │       │   │   │   image_gen_stream_event.py
    │       │   │   │   image_input_reference_param.py
    │       │   │   │   image_model.py
    │       │   │   │   model.py
    │       │   │   │   model_deleted.py
    │       │   │   │   moderation.py
    │       │   │   │   moderation_create_params.py
    │       │   │   │   moderation_create_response.py
    │       │   │   │   moderation_image_url_input_param.py
    │       │   │   │   moderation_model.py
    │       │   │   │   moderation_multi_modal_input_param.py
    │       │   │   │   moderation_text_input_param.py
    │       │   │   │   other_file_chunking_strategy_object.py
    │       │   │   │   skill.py
    │       │   │   │   skill_create_params.py
    │       │   │   │   skill_list.py
    │       │   │   │   skill_list_params.py
    │       │   │   │   skill_update_params.py
    │       │   │   │   static_file_chunking_strategy.py
    │       │   │   │   static_file_chunking_strategy_object.py
    │       │   │   │   static_file_chunking_strategy_object_param.py
    │       │   │   │   static_file_chunking_strategy_param.py
    │       │   │   │   upload.py
    │       │   │   │   upload_complete_params.py
    │       │   │   │   upload_create_params.py
    │       │   │   │   vector_store.py
    │       │   │   │   vector_store_create_params.py
    │       │   │   │   vector_store_deleted.py
    │       │   │   │   vector_store_list_params.py
    │       │   │   │   vector_store_search_params.py
    │       │   │   │   vector_store_search_response.py
    │       │   │   │   vector_store_update_params.py
    │       │   │   │   video.py
    │       │   │   │   video_create_character_params.py
    │       │   │   │   video_create_character_response.py
    │       │   │   │   video_create_error.py
    │       │   │   │   video_create_params.py
    │       │   │   │   video_delete_response.py
    │       │   │   │   video_download_content_params.py
    │       │   │   │   video_edit_params.py
    │       │   │   │   video_extend_params.py
    │       │   │   │   video_get_character_response.py
    │       │   │   │   video_list_params.py
    │       │   │   │   video_model.py
    │       │   │   │   video_model_param.py
    │       │   │   │   video_remix_params.py
    │       │   │   │   video_seconds.py
    │       │   │   │   video_size.py
    │       │   │   │   websocket_connection_options.py
    │       │   │   │   websocket_reconnection.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   ├───admin
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───organization
    │       │   │   │   │   │   admin_api_key.py
    │       │   │   │   │   │   admin_api_key_create_params.py
    │       │   │   │   │   │   admin_api_key_create_response.py
    │       │   │   │   │   │   admin_api_key_delete_response.py
    │       │   │   │   │   │   admin_api_key_list_params.py
    │       │   │   │   │   │   audit_log_list_params.py
    │       │   │   │   │   │   audit_log_list_response.py
    │       │   │   │   │   │   certificate.py
    │       │   │   │   │   │   certificate_activate_params.py
    │       │   │   │   │   │   certificate_activate_response.py
    │       │   │   │   │   │   certificate_create_params.py
    │       │   │   │   │   │   certificate_deactivate_params.py
    │       │   │   │   │   │   certificate_deactivate_response.py
    │       │   │   │   │   │   certificate_delete_response.py
    │       │   │   │   │   │   certificate_list_params.py
    │       │   │   │   │   │   certificate_list_response.py
    │       │   │   │   │   │   certificate_retrieve_params.py
    │       │   │   │   │   │   certificate_update_params.py
    │       │   │   │   │   │   data_retention_update_params.py
    │       │   │   │   │   │   group.py
    │       │   │   │   │   │   group_create_params.py
    │       │   │   │   │   │   group_delete_response.py
    │       │   │   │   │   │   group_list_params.py
    │       │   │   │   │   │   group_update_params.py
    │       │   │   │   │   │   group_update_response.py
    │       │   │   │   │   │   invite.py
    │       │   │   │   │   │   invite_create_params.py
    │       │   │   │   │   │   invite_delete_response.py
    │       │   │   │   │   │   invite_list_params.py
    │       │   │   │   │   │   organization_data_retention.py
    │       │   │   │   │   │   organization_spend_alert.py
    │       │   │   │   │   │   organization_spend_alert_deleted.py
    │       │   │   │   │   │   organization_spend_limit.py
    │       │   │   │   │   │   organization_spend_limit_deleted.py
    │       │   │   │   │   │   organization_user.py
    │       │   │   │   │   │   project.py
    │       │   │   │   │   │   project_create_params.py
    │       │   │   │   │   │   project_list_params.py
    │       │   │   │   │   │   project_update_params.py
    │       │   │   │   │   │   role.py
    │       │   │   │   │   │   role_create_params.py
    │       │   │   │   │   │   role_delete_response.py
    │       │   │   │   │   │   role_list_params.py
    │       │   │   │   │   │   role_update_params.py
    │       │   │   │   │   │   spend_alert_create_params.py
    │       │   │   │   │   │   spend_alert_list_params.py
    │       │   │   │   │   │   spend_alert_update_params.py
    │       │   │   │   │   │   spend_limit_update_params.py
    │       │   │   │   │   │   usage_audio_speeches_params.py
    │       │   │   │   │   │   usage_audio_speeches_response.py
    │       │   │   │   │   │   usage_audio_transcriptions_params.py
    │       │   │   │   │   │   usage_audio_transcriptions_response.py
    │       │   │   │   │   │   usage_code_interpreter_sessions_params.py
    │       │   │   │   │   │   usage_code_interpreter_sessions_response.py
    │       │   │   │   │   │   usage_completions_params.py
    │       │   │   │   │   │   usage_completions_response.py
    │       │   │   │   │   │   usage_costs_params.py
    │       │   │   │   │   │   usage_costs_response.py
    │       │   │   │   │   │   usage_embeddings_params.py
    │       │   │   │   │   │   usage_embeddings_response.py
    │       │   │   │   │   │   usage_file_search_calls_params.py
    │       │   │   │   │   │   usage_file_search_calls_response.py
    │       │   │   │   │   │   usage_images_params.py
    │       │   │   │   │   │   usage_images_response.py
    │       │   │   │   │   │   usage_moderations_params.py
    │       │   │   │   │   │   usage_moderations_response.py
    │       │   │   │   │   │   usage_vector_stores_params.py
    │       │   │   │   │   │   usage_vector_stores_response.py
    │       │   │   │   │   │   usage_web_search_calls_params.py
    │       │   │   │   │   │   usage_web_search_calls_response.py
    │       │   │   │   │   │   user_delete_response.py
    │       │   │   │   │   │   user_list_params.py
    │       │   │   │   │   │   user_update_params.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   ├───groups
    │       │   │   │   │   │   │   organization_group_user.py
    │       │   │   │   │   │   │   role_create_params.py
    │       │   │   │   │   │   │   role_create_response.py
    │       │   │   │   │   │   │   role_delete_response.py
    │       │   │   │   │   │   │   role_list_params.py
    │       │   │   │   │   │   │   role_list_response.py
    │       │   │   │   │   │   │   role_retrieve_response.py
    │       │   │   │   │   │   │   user_create_params.py
    │       │   │   │   │   │   │   user_create_response.py
    │       │   │   │   │   │   │   user_delete_response.py
    │       │   │   │   │   │   │   user_list_params.py
    │       │   │   │   │   │   │   user_retrieve_response.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           organization_group_user.cpython-314.pyc
    │       │   │   │   │   │           role_create_params.cpython-314.pyc
    │       │   │   │   │   │           role_create_response.cpython-314.pyc
    │       │   │   │   │   │           role_delete_response.cpython-314.pyc
    │       │   │   │   │   │           role_list_params.cpython-314.pyc
    │       │   │   │   │   │           role_list_response.cpython-314.pyc
    │       │   │   │   │   │           role_retrieve_response.cpython-314.pyc
    │       │   │   │   │   │           user_create_params.cpython-314.pyc
    │       │   │   │   │   │           user_create_response.cpython-314.pyc
    │       │   │   │   │   │           user_delete_response.cpython-314.pyc
    │       │   │   │   │   │           user_list_params.cpython-314.pyc
    │       │   │   │   │   │           user_retrieve_response.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   ├───projects
    │       │   │   │   │   │   │   api_key_delete_response.py
    │       │   │   │   │   │   │   api_key_list_params.py
    │       │   │   │   │   │   │   certificate_activate_params.py
    │       │   │   │   │   │   │   certificate_activate_response.py
    │       │   │   │   │   │   │   certificate_deactivate_params.py
    │       │   │   │   │   │   │   certificate_deactivate_response.py
    │       │   │   │   │   │   │   certificate_list_params.py
    │       │   │   │   │   │   │   certificate_list_response.py
    │       │   │   │   │   │   │   data_retention_update_params.py
    │       │   │   │   │   │   │   group_create_params.py
    │       │   │   │   │   │   │   group_delete_response.py
    │       │   │   │   │   │   │   group_list_params.py
    │       │   │   │   │   │   │   group_retrieve_params.py
    │       │   │   │   │   │   │   hosted_tool_permission_update_params.py
    │       │   │   │   │   │   │   model_permission_update_params.py
    │       │   │   │   │   │   │   project_api_key.py
    │       │   │   │   │   │   │   project_data_retention.py
    │       │   │   │   │   │   │   project_group.py
    │       │   │   │   │   │   │   project_hosted_tool_permissions.py
    │       │   │   │   │   │   │   project_model_permissions.py
    │       │   │   │   │   │   │   project_model_permissions_deleted.py
    │       │   │   │   │   │   │   project_rate_limit.py
    │       │   │   │   │   │   │   project_service_account.py
    │       │   │   │   │   │   │   project_spend_alert.py
    │       │   │   │   │   │   │   project_spend_alert_deleted.py
    │       │   │   │   │   │   │   project_spend_limit.py
    │       │   │   │   │   │   │   project_spend_limit_deleted.py
    │       │   │   │   │   │   │   project_user.py
    │       │   │   │   │   │   │   rate_limit_list_rate_limits_params.py
    │       │   │   │   │   │   │   rate_limit_update_rate_limit_params.py
    │       │   │   │   │   │   │   role_create_params.py
    │       │   │   │   │   │   │   role_delete_response.py
    │       │   │   │   │   │   │   role_list_params.py
    │       │   │   │   │   │   │   role_update_params.py
    │       │   │   │   │   │   │   service_account_create_params.py
    │       │   │   │   │   │   │   service_account_create_response.py
    │       │   │   │   │   │   │   service_account_delete_response.py
    │       │   │   │   │   │   │   service_account_list_params.py
    │       │   │   │   │   │   │   service_account_update_params.py
    │       │   │   │   │   │   │   spend_alert_create_params.py
    │       │   │   │   │   │   │   spend_alert_list_params.py
    │       │   │   │   │   │   │   spend_alert_update_params.py
    │       │   │   │   │   │   │   spend_limit_update_params.py
    │       │   │   │   │   │   │   user_create_params.py
    │       │   │   │   │   │   │   user_delete_response.py
    │       │   │   │   │   │   │   user_list_params.py
    │       │   │   │   │   │   │   user_update_params.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   ├───groups
    │       │   │   │   │   │   │   │   role_create_params.py
    │       │   │   │   │   │   │   │   role_create_response.py
    │       │   │   │   │   │   │   │   role_delete_response.py
    │       │   │   │   │   │   │   │   role_list_params.py
    │       │   │   │   │   │   │   │   role_list_response.py
    │       │   │   │   │   │   │   │   role_retrieve_response.py
    │       │   │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │   │
    │       │   │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │   │           role_create_params.cpython-314.pyc
    │       │   │   │   │   │   │           role_create_response.cpython-314.pyc
    │       │   │   │   │   │   │           role_delete_response.cpython-314.pyc
    │       │   │   │   │   │   │           role_list_params.cpython-314.pyc
    │       │   │   │   │   │   │           role_list_response.cpython-314.pyc
    │       │   │   │   │   │   │           role_retrieve_response.cpython-314.pyc
    │       │   │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │   │
    │       │   │   │   │   │   ├───service_accounts
    │       │   │   │   │   │   │   │   api_key_create_params.py
    │       │   │   │   │   │   │   │   api_key_create_response.py
    │       │   │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │   │
    │       │   │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │   │           api_key_create_params.cpython-314.pyc
    │       │   │   │   │   │   │           api_key_create_response.cpython-314.pyc
    │       │   │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │   │
    │       │   │   │   │   │   ├───users
    │       │   │   │   │   │   │   │   role_create_params.py
    │       │   │   │   │   │   │   │   role_create_response.py
    │       │   │   │   │   │   │   │   role_delete_response.py
    │       │   │   │   │   │   │   │   role_list_params.py
    │       │   │   │   │   │   │   │   role_list_response.py
    │       │   │   │   │   │   │   │   role_retrieve_response.py
    │       │   │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │   │
    │       │   │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │   │           role_create_params.cpython-314.pyc
    │       │   │   │   │   │   │           role_create_response.cpython-314.pyc
    │       │   │   │   │   │   │           role_delete_response.cpython-314.pyc
    │       │   │   │   │   │   │           role_list_params.cpython-314.pyc
    │       │   │   │   │   │   │           role_list_response.cpython-314.pyc
    │       │   │   │   │   │   │           role_retrieve_response.cpython-314.pyc
    │       │   │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           api_key_delete_response.cpython-314.pyc
    │       │   │   │   │   │           api_key_list_params.cpython-314.pyc
    │       │   │   │   │   │           certificate_activate_params.cpython-314.pyc
    │       │   │   │   │   │           certificate_activate_response.cpython-314.pyc
    │       │   │   │   │   │           certificate_deactivate_params.cpython-314.pyc
    │       │   │   │   │   │           certificate_deactivate_response.cpython-314.pyc
    │       │   │   │   │   │           certificate_list_params.cpython-314.pyc
    │       │   │   │   │   │           certificate_list_response.cpython-314.pyc
    │       │   │   │   │   │           data_retention_update_params.cpython-314.pyc
    │       │   │   │   │   │           group_create_params.cpython-314.pyc
    │       │   │   │   │   │           group_delete_response.cpython-314.pyc
    │       │   │   │   │   │           group_list_params.cpython-314.pyc
    │       │   │   │   │   │           group_retrieve_params.cpython-314.pyc
    │       │   │   │   │   │           hosted_tool_permission_update_params.cpython-314.pyc
    │       │   │   │   │   │           model_permission_update_params.cpython-314.pyc
    │       │   │   │   │   │           project_api_key.cpython-314.pyc
    │       │   │   │   │   │           project_data_retention.cpython-314.pyc
    │       │   │   │   │   │           project_group.cpython-314.pyc
    │       │   │   │   │   │           project_hosted_tool_permissions.cpython-314.pyc
    │       │   │   │   │   │           project_model_permissions.cpython-314.pyc
    │       │   │   │   │   │           project_model_permissions_deleted.cpython-314.pyc
    │       │   │   │   │   │           project_rate_limit.cpython-314.pyc
    │       │   │   │   │   │           project_service_account.cpython-314.pyc
    │       │   │   │   │   │           project_spend_alert.cpython-314.pyc
    │       │   │   │   │   │           project_spend_alert_deleted.cpython-314.pyc
    │       │   │   │   │   │           project_spend_limit.cpython-314.pyc
    │       │   │   │   │   │           project_spend_limit_deleted.cpython-314.pyc
    │       │   │   │   │   │           project_user.cpython-314.pyc
    │       │   │   │   │   │           rate_limit_list_rate_limits_params.cpython-314.pyc
    │       │   │   │   │   │           rate_limit_update_rate_limit_params.cpython-314.pyc
    │       │   │   │   │   │           role_create_params.cpython-314.pyc
    │       │   │   │   │   │           role_delete_response.cpython-314.pyc
    │       │   │   │   │   │           role_list_params.cpython-314.pyc
    │       │   │   │   │   │           role_update_params.cpython-314.pyc
    │       │   │   │   │   │           service_account_create_params.cpython-314.pyc
    │       │   │   │   │   │           service_account_create_response.cpython-314.pyc
    │       │   │   │   │   │           service_account_delete_response.cpython-314.pyc
    │       │   │   │   │   │           service_account_list_params.cpython-314.pyc
    │       │   │   │   │   │           service_account_update_params.cpython-314.pyc
    │       │   │   │   │   │           spend_alert_create_params.cpython-314.pyc
    │       │   │   │   │   │           spend_alert_list_params.cpython-314.pyc
    │       │   │   │   │   │           spend_alert_update_params.cpython-314.pyc
    │       │   │   │   │   │           spend_limit_update_params.cpython-314.pyc
    │       │   │   │   │   │           user_create_params.cpython-314.pyc
    │       │   │   │   │   │           user_delete_response.cpython-314.pyc
    │       │   │   │   │   │           user_list_params.cpython-314.pyc
    │       │   │   │   │   │           user_update_params.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   ├───users
    │       │   │   │   │   │   │   role_create_params.py
    │       │   │   │   │   │   │   role_create_response.py
    │       │   │   │   │   │   │   role_delete_response.py
    │       │   │   │   │   │   │   role_list_params.py
    │       │   │   │   │   │   │   role_list_response.py
    │       │   │   │   │   │   │   role_retrieve_response.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           role_create_params.cpython-314.pyc
    │       │   │   │   │   │           role_create_response.cpython-314.pyc
    │       │   │   │   │   │           role_delete_response.cpython-314.pyc
    │       │   │   │   │   │           role_list_params.cpython-314.pyc
    │       │   │   │   │   │           role_list_response.cpython-314.pyc
    │       │   │   │   │   │           role_retrieve_response.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           admin_api_key.cpython-314.pyc
    │       │   │   │   │           admin_api_key_create_params.cpython-314.pyc
    │       │   │   │   │           admin_api_key_create_response.cpython-314.pyc
    │       │   │   │   │           admin_api_key_delete_response.cpython-314.pyc
    │       │   │   │   │           admin_api_key_list_params.cpython-314.pyc
    │       │   │   │   │           audit_log_list_params.cpython-314.pyc
    │       │   │   │   │           audit_log_list_response.cpython-314.pyc
    │       │   │   │   │           certificate.cpython-314.pyc
    │       │   │   │   │           certificate_activate_params.cpython-314.pyc
    │       │   │   │   │           certificate_activate_response.cpython-314.pyc
    │       │   │   │   │           certificate_create_params.cpython-314.pyc
    │       │   │   │   │           certificate_deactivate_params.cpython-314.pyc
    │       │   │   │   │           certificate_deactivate_response.cpython-314.pyc
    │       │   │   │   │           certificate_delete_response.cpython-314.pyc
    │       │   │   │   │           certificate_list_params.cpython-314.pyc
    │       │   │   │   │           certificate_list_response.cpython-314.pyc
    │       │   │   │   │           certificate_retrieve_params.cpython-314.pyc
    │       │   │   │   │           certificate_update_params.cpython-314.pyc
    │       │   │   │   │           data_retention_update_params.cpython-314.pyc
    │       │   │   │   │           group.cpython-314.pyc
    │       │   │   │   │           group_create_params.cpython-314.pyc
    │       │   │   │   │           group_delete_response.cpython-314.pyc
    │       │   │   │   │           group_list_params.cpython-314.pyc
    │       │   │   │   │           group_update_params.cpython-314.pyc
    │       │   │   │   │           group_update_response.cpython-314.pyc
    │       │   │   │   │           invite.cpython-314.pyc
    │       │   │   │   │           invite_create_params.cpython-314.pyc
    │       │   │   │   │           invite_delete_response.cpython-314.pyc
    │       │   │   │   │           invite_list_params.cpython-314.pyc
    │       │   │   │   │           organization_data_retention.cpython-314.pyc
    │       │   │   │   │           organization_spend_alert.cpython-314.pyc
    │       │   │   │   │           organization_spend_alert_deleted.cpython-314.pyc
    │       │   │   │   │           organization_spend_limit.cpython-314.pyc
    │       │   │   │   │           organization_spend_limit_deleted.cpython-314.pyc
    │       │   │   │   │           organization_user.cpython-314.pyc
    │       │   │   │   │           project.cpython-314.pyc
    │       │   │   │   │           project_create_params.cpython-314.pyc
    │       │   │   │   │           project_list_params.cpython-314.pyc
    │       │   │   │   │           project_update_params.cpython-314.pyc
    │       │   │   │   │           role.cpython-314.pyc
    │       │   │   │   │           role_create_params.cpython-314.pyc
    │       │   │   │   │           role_delete_response.cpython-314.pyc
    │       │   │   │   │           role_list_params.cpython-314.pyc
    │       │   │   │   │           role_update_params.cpython-314.pyc
    │       │   │   │   │           spend_alert_create_params.cpython-314.pyc
    │       │   │   │   │           spend_alert_list_params.cpython-314.pyc
    │       │   │   │   │           spend_alert_update_params.cpython-314.pyc
    │       │   │   │   │           spend_limit_update_params.cpython-314.pyc
    │       │   │   │   │           usage_audio_speeches_params.cpython-314.pyc
    │       │   │   │   │           usage_audio_speeches_response.cpython-314.pyc
    │       │   │   │   │           usage_audio_transcriptions_params.cpython-314.pyc
    │       │   │   │   │           usage_audio_transcriptions_response.cpython-314.pyc
    │       │   │   │   │           usage_code_interpreter_sessions_params.cpython-314.pyc
    │       │   │   │   │           usage_code_interpreter_sessions_response.cpython-314.pyc
    │       │   │   │   │           usage_completions_params.cpython-314.pyc
    │       │   │   │   │           usage_completions_response.cpython-314.pyc
    │       │   │   │   │           usage_costs_params.cpython-314.pyc
    │       │   │   │   │           usage_costs_response.cpython-314.pyc
    │       │   │   │   │           usage_embeddings_params.cpython-314.pyc
    │       │   │   │   │           usage_embeddings_response.cpython-314.pyc
    │       │   │   │   │           usage_file_search_calls_params.cpython-314.pyc
    │       │   │   │   │           usage_file_search_calls_response.cpython-314.pyc
    │       │   │   │   │           usage_images_params.cpython-314.pyc
    │       │   │   │   │           usage_images_response.cpython-314.pyc
    │       │   │   │   │           usage_moderations_params.cpython-314.pyc
    │       │   │   │   │           usage_moderations_response.cpython-314.pyc
    │       │   │   │   │           usage_vector_stores_params.cpython-314.pyc
    │       │   │   │   │           usage_vector_stores_response.cpython-314.pyc
    │       │   │   │   │           usage_web_search_calls_params.cpython-314.pyc
    │       │   │   │   │           usage_web_search_calls_response.cpython-314.pyc
    │       │   │   │   │           user_delete_response.cpython-314.pyc
    │       │   │   │   │           user_list_params.cpython-314.pyc
    │       │   │   │   │           user_update_params.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───audio
    │       │   │   │   │   speech_create_params.py
    │       │   │   │   │   speech_model.py
    │       │   │   │   │   transcription.py
    │       │   │   │   │   transcription_create_params.py
    │       │   │   │   │   transcription_create_response.py
    │       │   │   │   │   transcription_diarized.py
    │       │   │   │   │   transcription_diarized_segment.py
    │       │   │   │   │   transcription_include.py
    │       │   │   │   │   transcription_segment.py
    │       │   │   │   │   transcription_stream_event.py
    │       │   │   │   │   transcription_text_delta_event.py
    │       │   │   │   │   transcription_text_done_event.py
    │       │   │   │   │   transcription_text_segment_event.py
    │       │   │   │   │   transcription_verbose.py
    │       │   │   │   │   transcription_word.py
    │       │   │   │   │   translation.py
    │       │   │   │   │   translation_create_params.py
    │       │   │   │   │   translation_create_response.py
    │       │   │   │   │   translation_verbose.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           speech_create_params.cpython-314.pyc
    │       │   │   │           speech_model.cpython-314.pyc
    │       │   │   │           transcription.cpython-314.pyc
    │       │   │   │           transcription_create_params.cpython-314.pyc
    │       │   │   │           transcription_create_response.cpython-314.pyc
    │       │   │   │           transcription_diarized.cpython-314.pyc
    │       │   │   │           transcription_diarized_segment.cpython-314.pyc
    │       │   │   │           transcription_include.cpython-314.pyc
    │       │   │   │           transcription_segment.cpython-314.pyc
    │       │   │   │           transcription_stream_event.cpython-314.pyc
    │       │   │   │           transcription_text_delta_event.cpython-314.pyc
    │       │   │   │           transcription_text_done_event.cpython-314.pyc
    │       │   │   │           transcription_text_segment_event.cpython-314.pyc
    │       │   │   │           transcription_verbose.cpython-314.pyc
    │       │   │   │           transcription_word.cpython-314.pyc
    │       │   │   │           translation.cpython-314.pyc
    │       │   │   │           translation_create_params.cpython-314.pyc
    │       │   │   │           translation_create_response.cpython-314.pyc
    │       │   │   │           translation_verbose.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───beta
    │       │   │   │   │   assistant.py
    │       │   │   │   │   assistant_create_params.py
    │       │   │   │   │   assistant_deleted.py
    │       │   │   │   │   assistant_list_params.py
    │       │   │   │   │   assistant_response_format_option.py
    │       │   │   │   │   assistant_response_format_option_param.py
    │       │   │   │   │   assistant_stream_event.py
    │       │   │   │   │   assistant_tool.py
    │       │   │   │   │   assistant_tool_choice.py
    │       │   │   │   │   assistant_tool_choice_function.py
    │       │   │   │   │   assistant_tool_choice_function_param.py
    │       │   │   │   │   assistant_tool_choice_option.py
    │       │   │   │   │   assistant_tool_choice_option_param.py
    │       │   │   │   │   assistant_tool_choice_param.py
    │       │   │   │   │   assistant_tool_param.py
    │       │   │   │   │   assistant_update_params.py
    │       │   │   │   │   beta_apply_patch_tool.py
    │       │   │   │   │   beta_apply_patch_tool_param.py
    │       │   │   │   │   beta_compacted_response.py
    │       │   │   │   │   beta_computer_action.py
    │       │   │   │   │   beta_computer_action_list.py
    │       │   │   │   │   beta_computer_action_list_param.py
    │       │   │   │   │   beta_computer_action_param.py
    │       │   │   │   │   beta_computer_tool.py
    │       │   │   │   │   beta_computer_tool_param.py
    │       │   │   │   │   beta_computer_use_preview_tool.py
    │       │   │   │   │   beta_computer_use_preview_tool_param.py
    │       │   │   │   │   beta_container_auto.py
    │       │   │   │   │   beta_container_auto_param.py
    │       │   │   │   │   beta_container_network_policy_allowlist.py
    │       │   │   │   │   beta_container_network_policy_allowlist_param.py
    │       │   │   │   │   beta_container_network_policy_disabled.py
    │       │   │   │   │   beta_container_network_policy_disabled_param.py
    │       │   │   │   │   beta_container_network_policy_domain_secret.py
    │       │   │   │   │   beta_container_network_policy_domain_secret_param.py
    │       │   │   │   │   beta_container_reference.py
    │       │   │   │   │   beta_container_reference_param.py
    │       │   │   │   │   beta_custom_tool.py
    │       │   │   │   │   beta_custom_tool_param.py
    │       │   │   │   │   beta_easy_input_message.py
    │       │   │   │   │   beta_easy_input_message_param.py
    │       │   │   │   │   beta_file_search_tool.py
    │       │   │   │   │   beta_file_search_tool_param.py
    │       │   │   │   │   beta_function_shell_tool.py
    │       │   │   │   │   beta_function_shell_tool_param.py
    │       │   │   │   │   beta_function_tool.py
    │       │   │   │   │   beta_function_tool_param.py
    │       │   │   │   │   beta_inline_skill.py
    │       │   │   │   │   beta_inline_skill_param.py
    │       │   │   │   │   beta_inline_skill_source.py
    │       │   │   │   │   beta_inline_skill_source_param.py
    │       │   │   │   │   beta_local_environment.py
    │       │   │   │   │   beta_local_environment_param.py
    │       │   │   │   │   beta_local_skill.py
    │       │   │   │   │   beta_local_skill_param.py
    │       │   │   │   │   beta_namespace_tool.py
    │       │   │   │   │   beta_namespace_tool_param.py
    │       │   │   │   │   beta_response.py
    │       │   │   │   │   beta_responses_client_event.py
    │       │   │   │   │   beta_responses_client_event_param.py
    │       │   │   │   │   beta_responses_server_event.py
    │       │   │   │   │   beta_response_apply_patch_tool_call.py
    │       │   │   │   │   beta_response_apply_patch_tool_call_output.py
    │       │   │   │   │   beta_response_audio_delta_event.py
    │       │   │   │   │   beta_response_audio_done_event.py
    │       │   │   │   │   beta_response_audio_transcript_delta_event.py
    │       │   │   │   │   beta_response_audio_transcript_done_event.py
    │       │   │   │   │   beta_response_code_interpreter_call_code_delta_event.py
    │       │   │   │   │   beta_response_code_interpreter_call_code_done_event.py
    │       │   │   │   │   beta_response_code_interpreter_call_completed_event.py
    │       │   │   │   │   beta_response_code_interpreter_call_interpreting_event.py
    │       │   │   │   │   beta_response_code_interpreter_call_in_progress_event.py
    │       │   │   │   │   beta_response_code_interpreter_tool_call.py
    │       │   │   │   │   beta_response_code_interpreter_tool_call_param.py
    │       │   │   │   │   beta_response_compaction_item.py
    │       │   │   │   │   beta_response_compaction_item_param.py
    │       │   │   │   │   beta_response_compaction_item_param_param.py
    │       │   │   │   │   beta_response_completed_event.py
    │       │   │   │   │   beta_response_computer_tool_call.py
    │       │   │   │   │   beta_response_computer_tool_call_output_item.py
    │       │   │   │   │   beta_response_computer_tool_call_output_screenshot.py
    │       │   │   │   │   beta_response_computer_tool_call_output_screenshot_param.py
    │       │   │   │   │   beta_response_computer_tool_call_param.py
    │       │   │   │   │   beta_response_container_reference.py
    │       │   │   │   │   beta_response_content_part_added_event.py
    │       │   │   │   │   beta_response_content_part_done_event.py
    │       │   │   │   │   beta_response_conversation_param.py
    │       │   │   │   │   beta_response_conversation_param_param.py
    │       │   │   │   │   beta_response_created_event.py
    │       │   │   │   │   beta_response_custom_tool_call.py
    │       │   │   │   │   beta_response_custom_tool_call_input_delta_event.py
    │       │   │   │   │   beta_response_custom_tool_call_input_done_event.py
    │       │   │   │   │   beta_response_custom_tool_call_item.py
    │       │   │   │   │   beta_response_custom_tool_call_output.py
    │       │   │   │   │   beta_response_custom_tool_call_output_item.py
    │       │   │   │   │   beta_response_custom_tool_call_output_param.py
    │       │   │   │   │   beta_response_custom_tool_call_param.py
    │       │   │   │   │   beta_response_error.py
    │       │   │   │   │   beta_response_error_event.py
    │       │   │   │   │   beta_response_failed_event.py
    │       │   │   │   │   beta_response_file_search_call_completed_event.py
    │       │   │   │   │   beta_response_file_search_call_in_progress_event.py
    │       │   │   │   │   beta_response_file_search_call_searching_event.py
    │       │   │   │   │   beta_response_file_search_tool_call.py
    │       │   │   │   │   beta_response_file_search_tool_call_param.py
    │       │   │   │   │   beta_response_format_text_config.py
    │       │   │   │   │   beta_response_format_text_config_param.py
    │       │   │   │   │   beta_response_format_text_json_schema_config.py
    │       │   │   │   │   beta_response_format_text_json_schema_config_param.py
    │       │   │   │   │   beta_response_function_call_arguments_delta_event.py
    │       │   │   │   │   beta_response_function_call_arguments_done_event.py
    │       │   │   │   │   beta_response_function_call_output_item.py
    │       │   │   │   │   beta_response_function_call_output_item_list.py
    │       │   │   │   │   beta_response_function_call_output_item_list_param.py
    │       │   │   │   │   beta_response_function_call_output_item_param.py
    │       │   │   │   │   beta_response_function_shell_call_output_content.py
    │       │   │   │   │   beta_response_function_shell_call_output_content_param.py
    │       │   │   │   │   beta_response_function_shell_tool_call.py
    │       │   │   │   │   beta_response_function_shell_tool_call_output.py
    │       │   │   │   │   beta_response_function_tool_call.py
    │       │   │   │   │   beta_response_function_tool_call_item.py
    │       │   │   │   │   beta_response_function_tool_call_output_item.py
    │       │   │   │   │   beta_response_function_tool_call_param.py
    │       │   │   │   │   beta_response_function_web_search.py
    │       │   │   │   │   beta_response_function_web_search_param.py
    │       │   │   │   │   beta_response_image_gen_call_completed_event.py
    │       │   │   │   │   beta_response_image_gen_call_generating_event.py
    │       │   │   │   │   beta_response_image_gen_call_in_progress_event.py
    │       │   │   │   │   beta_response_image_gen_call_partial_image_event.py
    │       │   │   │   │   beta_response_includable.py
    │       │   │   │   │   beta_response_incomplete_event.py
    │       │   │   │   │   beta_response_inject_created_event.py
    │       │   │   │   │   beta_response_inject_event.py
    │       │   │   │   │   beta_response_inject_event_param.py
    │       │   │   │   │   beta_response_inject_failed_event.py
    │       │   │   │   │   beta_response_input.py
    │       │   │   │   │   beta_response_input_content.py
    │       │   │   │   │   beta_response_input_content_param.py
    │       │   │   │   │   beta_response_input_file.py
    │       │   │   │   │   beta_response_input_file_content.py
    │       │   │   │   │   beta_response_input_file_content_param.py
    │       │   │   │   │   beta_response_input_file_param.py
    │       │   │   │   │   beta_response_input_image.py
    │       │   │   │   │   beta_response_input_image_content.py
    │       │   │   │   │   beta_response_input_image_content_param.py
    │       │   │   │   │   beta_response_input_image_param.py
    │       │   │   │   │   beta_response_input_item.py
    │       │   │   │   │   beta_response_input_item_param.py
    │       │   │   │   │   beta_response_input_message_content_list.py
    │       │   │   │   │   beta_response_input_message_content_list_param.py
    │       │   │   │   │   beta_response_input_message_item.py
    │       │   │   │   │   beta_response_input_param.py
    │       │   │   │   │   beta_response_input_text.py
    │       │   │   │   │   beta_response_input_text_content.py
    │       │   │   │   │   beta_response_input_text_content_param.py
    │       │   │   │   │   beta_response_input_text_param.py
    │       │   │   │   │   beta_response_in_progress_event.py
    │       │   │   │   │   beta_response_item.py
    │       │   │   │   │   beta_response_local_environment.py
    │       │   │   │   │   beta_response_mcp_call_arguments_delta_event.py
    │       │   │   │   │   beta_response_mcp_call_arguments_done_event.py
    │       │   │   │   │   beta_response_mcp_call_completed_event.py
    │       │   │   │   │   beta_response_mcp_call_failed_event.py
    │       │   │   │   │   beta_response_mcp_call_in_progress_event.py
    │       │   │   │   │   beta_response_mcp_list_tools_completed_event.py
    │       │   │   │   │   beta_response_mcp_list_tools_failed_event.py
    │       │   │   │   │   beta_response_mcp_list_tools_in_progress_event.py
    │       │   │   │   │   beta_response_output_item.py
    │       │   │   │   │   beta_response_output_item_added_event.py
    │       │   │   │   │   beta_response_output_item_done_event.py
    │       │   │   │   │   beta_response_output_message.py
    │       │   │   │   │   beta_response_output_message_param.py
    │       │   │   │   │   beta_response_output_refusal.py
    │       │   │   │   │   beta_response_output_refusal_param.py
    │       │   │   │   │   beta_response_output_text.py
    │       │   │   │   │   beta_response_output_text_annotation_added_event.py
    │       │   │   │   │   beta_response_output_text_param.py
    │       │   │   │   │   beta_response_prompt.py
    │       │   │   │   │   beta_response_prompt_param.py
    │       │   │   │   │   beta_response_queued_event.py
    │       │   │   │   │   beta_response_reasoning_item.py
    │       │   │   │   │   beta_response_reasoning_item_param.py
    │       │   │   │   │   beta_response_reasoning_summary_part_added_event.py
    │       │   │   │   │   beta_response_reasoning_summary_part_done_event.py
    │       │   │   │   │   beta_response_reasoning_summary_text_delta_event.py
    │       │   │   │   │   beta_response_reasoning_summary_text_done_event.py
    │       │   │   │   │   beta_response_reasoning_text_delta_event.py
    │       │   │   │   │   beta_response_reasoning_text_done_event.py
    │       │   │   │   │   beta_response_refusal_delta_event.py
    │       │   │   │   │   beta_response_refusal_done_event.py
    │       │   │   │   │   beta_response_status.py
    │       │   │   │   │   beta_response_stream_event.py
    │       │   │   │   │   beta_response_text_config.py
    │       │   │   │   │   beta_response_text_config_param.py
    │       │   │   │   │   beta_response_text_delta_event.py
    │       │   │   │   │   beta_response_text_done_event.py
    │       │   │   │   │   beta_response_tool_search_call.py
    │       │   │   │   │   beta_response_tool_search_output_item.py
    │       │   │   │   │   beta_response_tool_search_output_item_param.py
    │       │   │   │   │   beta_response_tool_search_output_item_param_param.py
    │       │   │   │   │   beta_response_usage.py
    │       │   │   │   │   beta_response_web_search_call_completed_event.py
    │       │   │   │   │   beta_response_web_search_call_in_progress_event.py
    │       │   │   │   │   beta_response_web_search_call_searching_event.py
    │       │   │   │   │   beta_skill_reference.py
    │       │   │   │   │   beta_skill_reference_param.py
    │       │   │   │   │   beta_tool.py
    │       │   │   │   │   beta_tool_choice_allowed.py
    │       │   │   │   │   beta_tool_choice_allowed_param.py
    │       │   │   │   │   beta_tool_choice_apply_patch.py
    │       │   │   │   │   beta_tool_choice_apply_patch_param.py
    │       │   │   │   │   beta_tool_choice_custom.py
    │       │   │   │   │   beta_tool_choice_custom_param.py
    │       │   │   │   │   beta_tool_choice_function.py
    │       │   │   │   │   beta_tool_choice_function_param.py
    │       │   │   │   │   beta_tool_choice_mcp.py
    │       │   │   │   │   beta_tool_choice_mcp_param.py
    │       │   │   │   │   beta_tool_choice_options.py
    │       │   │   │   │   beta_tool_choice_shell.py
    │       │   │   │   │   beta_tool_choice_shell_param.py
    │       │   │   │   │   beta_tool_choice_types.py
    │       │   │   │   │   beta_tool_choice_types_param.py
    │       │   │   │   │   beta_tool_param.py
    │       │   │   │   │   beta_tool_search_tool.py
    │       │   │   │   │   beta_tool_search_tool_param.py
    │       │   │   │   │   beta_web_search_preview_tool.py
    │       │   │   │   │   beta_web_search_preview_tool_param.py
    │       │   │   │   │   beta_web_search_tool.py
    │       │   │   │   │   beta_web_search_tool_param.py
    │       │   │   │   │   chatkit_workflow.py
    │       │   │   │   │   code_interpreter_tool.py
    │       │   │   │   │   code_interpreter_tool_param.py
    │       │   │   │   │   file_search_tool.py
    │       │   │   │   │   file_search_tool_param.py
    │       │   │   │   │   function_tool.py
    │       │   │   │   │   function_tool_param.py
    │       │   │   │   │   response_compact_params.py
    │       │   │   │   │   response_create_params.py
    │       │   │   │   │   response_retrieve_params.py
    │       │   │   │   │   thread.py
    │       │   │   │   │   thread_create_and_run_params.py
    │       │   │   │   │   thread_create_params.py
    │       │   │   │   │   thread_deleted.py
    │       │   │   │   │   thread_update_params.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───chat
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───chatkit
    │       │   │   │   │   │   chatkit_attachment.py
    │       │   │   │   │   │   chatkit_response_output_text.py
    │       │   │   │   │   │   chatkit_thread.py
    │       │   │   │   │   │   chatkit_thread_assistant_message_item.py
    │       │   │   │   │   │   chatkit_thread_item_list.py
    │       │   │   │   │   │   chatkit_thread_user_message_item.py
    │       │   │   │   │   │   chatkit_widget_item.py
    │       │   │   │   │   │   chat_session.py
    │       │   │   │   │   │   chat_session_automatic_thread_titling.py
    │       │   │   │   │   │   chat_session_chatkit_configuration.py
    │       │   │   │   │   │   chat_session_chatkit_configuration_param.py
    │       │   │   │   │   │   chat_session_expires_after_param.py
    │       │   │   │   │   │   chat_session_file_upload.py
    │       │   │   │   │   │   chat_session_history.py
    │       │   │   │   │   │   chat_session_rate_limits.py
    │       │   │   │   │   │   chat_session_rate_limits_param.py
    │       │   │   │   │   │   chat_session_status.py
    │       │   │   │   │   │   chat_session_workflow_param.py
    │       │   │   │   │   │   session_create_params.py
    │       │   │   │   │   │   thread_delete_response.py
    │       │   │   │   │   │   thread_list_items_params.py
    │       │   │   │   │   │   thread_list_params.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           chatkit_attachment.cpython-314.pyc
    │       │   │   │   │           chatkit_response_output_text.cpython-314.pyc
    │       │   │   │   │           chatkit_thread.cpython-314.pyc
    │       │   │   │   │           chatkit_thread_assistant_message_item.cpython-314.pyc
    │       │   │   │   │           chatkit_thread_item_list.cpython-314.pyc
    │       │   │   │   │           chatkit_thread_user_message_item.cpython-314.pyc
    │       │   │   │   │           chatkit_widget_item.cpython-314.pyc
    │       │   │   │   │           chat_session.cpython-314.pyc
    │       │   │   │   │           chat_session_automatic_thread_titling.cpython-314.pyc
    │       │   │   │   │           chat_session_chatkit_configuration.cpython-314.pyc
    │       │   │   │   │           chat_session_chatkit_configuration_param.cpython-314.pyc
    │       │   │   │   │           chat_session_expires_after_param.cpython-314.pyc
    │       │   │   │   │           chat_session_file_upload.cpython-314.pyc
    │       │   │   │   │           chat_session_history.cpython-314.pyc
    │       │   │   │   │           chat_session_rate_limits.cpython-314.pyc
    │       │   │   │   │           chat_session_rate_limits_param.cpython-314.pyc
    │       │   │   │   │           chat_session_status.cpython-314.pyc
    │       │   │   │   │           chat_session_workflow_param.cpython-314.pyc
    │       │   │   │   │           session_create_params.cpython-314.pyc
    │       │   │   │   │           thread_delete_response.cpython-314.pyc
    │       │   │   │   │           thread_list_items_params.cpython-314.pyc
    │       │   │   │   │           thread_list_params.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───realtime
    │       │   │   │   │   │   conversation_created_event.py
    │       │   │   │   │   │   conversation_item.py
    │       │   │   │   │   │   conversation_item_content.py
    │       │   │   │   │   │   conversation_item_content_param.py
    │       │   │   │   │   │   conversation_item_created_event.py
    │       │   │   │   │   │   conversation_item_create_event.py
    │       │   │   │   │   │   conversation_item_create_event_param.py
    │       │   │   │   │   │   conversation_item_deleted_event.py
    │       │   │   │   │   │   conversation_item_delete_event.py
    │       │   │   │   │   │   conversation_item_delete_event_param.py
    │       │   │   │   │   │   conversation_item_input_audio_transcription_completed_event.py
    │       │   │   │   │   │   conversation_item_input_audio_transcription_delta_event.py
    │       │   │   │   │   │   conversation_item_input_audio_transcription_failed_event.py
    │       │   │   │   │   │   conversation_item_param.py
    │       │   │   │   │   │   conversation_item_retrieve_event.py
    │       │   │   │   │   │   conversation_item_retrieve_event_param.py
    │       │   │   │   │   │   conversation_item_truncated_event.py
    │       │   │   │   │   │   conversation_item_truncate_event.py
    │       │   │   │   │   │   conversation_item_truncate_event_param.py
    │       │   │   │   │   │   conversation_item_with_reference.py
    │       │   │   │   │   │   conversation_item_with_reference_param.py
    │       │   │   │   │   │   error_event.py
    │       │   │   │   │   │   input_audio_buffer_append_event.py
    │       │   │   │   │   │   input_audio_buffer_append_event_param.py
    │       │   │   │   │   │   input_audio_buffer_cleared_event.py
    │       │   │   │   │   │   input_audio_buffer_clear_event.py
    │       │   │   │   │   │   input_audio_buffer_clear_event_param.py
    │       │   │   │   │   │   input_audio_buffer_committed_event.py
    │       │   │   │   │   │   input_audio_buffer_commit_event.py
    │       │   │   │   │   │   input_audio_buffer_commit_event_param.py
    │       │   │   │   │   │   input_audio_buffer_speech_started_event.py
    │       │   │   │   │   │   input_audio_buffer_speech_stopped_event.py
    │       │   │   │   │   │   rate_limits_updated_event.py
    │       │   │   │   │   │   realtime_client_event.py
    │       │   │   │   │   │   realtime_client_event_param.py
    │       │   │   │   │   │   realtime_connect_params.py
    │       │   │   │   │   │   realtime_response.py
    │       │   │   │   │   │   realtime_response_status.py
    │       │   │   │   │   │   realtime_response_usage.py
    │       │   │   │   │   │   realtime_server_event.py
    │       │   │   │   │   │   response_audio_delta_event.py
    │       │   │   │   │   │   response_audio_done_event.py
    │       │   │   │   │   │   response_audio_transcript_delta_event.py
    │       │   │   │   │   │   response_audio_transcript_done_event.py
    │       │   │   │   │   │   response_cancel_event.py
    │       │   │   │   │   │   response_cancel_event_param.py
    │       │   │   │   │   │   response_content_part_added_event.py
    │       │   │   │   │   │   response_content_part_done_event.py
    │       │   │   │   │   │   response_created_event.py
    │       │   │   │   │   │   response_create_event.py
    │       │   │   │   │   │   response_create_event_param.py
    │       │   │   │   │   │   response_done_event.py
    │       │   │   │   │   │   response_function_call_arguments_delta_event.py
    │       │   │   │   │   │   response_function_call_arguments_done_event.py
    │       │   │   │   │   │   response_output_item_added_event.py
    │       │   │   │   │   │   response_output_item_done_event.py
    │       │   │   │   │   │   response_text_delta_event.py
    │       │   │   │   │   │   response_text_done_event.py
    │       │   │   │   │   │   session.py
    │       │   │   │   │   │   session_created_event.py
    │       │   │   │   │   │   session_create_params.py
    │       │   │   │   │   │   session_create_response.py
    │       │   │   │   │   │   session_updated_event.py
    │       │   │   │   │   │   session_update_event.py
    │       │   │   │   │   │   session_update_event_param.py
    │       │   │   │   │   │   transcription_session.py
    │       │   │   │   │   │   transcription_session_create_params.py
    │       │   │   │   │   │   transcription_session_update.py
    │       │   │   │   │   │   transcription_session_updated_event.py
    │       │   │   │   │   │   transcription_session_update_param.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           conversation_created_event.cpython-314.pyc
    │       │   │   │   │           conversation_item.cpython-314.pyc
    │       │   │   │   │           conversation_item_content.cpython-314.pyc
    │       │   │   │   │           conversation_item_content_param.cpython-314.pyc
    │       │   │   │   │           conversation_item_created_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_create_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_create_event_param.cpython-314.pyc
    │       │   │   │   │           conversation_item_deleted_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_delete_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_delete_event_param.cpython-314.pyc
    │       │   │   │   │           conversation_item_input_audio_transcription_completed_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_input_audio_transcription_delta_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_input_audio_transcription_failed_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_param.cpython-314.pyc
    │       │   │   │   │           conversation_item_retrieve_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_retrieve_event_param.cpython-314.pyc
    │       │   │   │   │           conversation_item_truncated_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_truncate_event.cpython-314.pyc
    │       │   │   │   │           conversation_item_truncate_event_param.cpython-314.pyc
    │       │   │   │   │           conversation_item_with_reference.cpython-314.pyc
    │       │   │   │   │           conversation_item_with_reference_param.cpython-314.pyc
    │       │   │   │   │           error_event.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_append_event.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_append_event_param.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_cleared_event.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_clear_event.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_clear_event_param.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_committed_event.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_commit_event.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_commit_event_param.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_speech_started_event.cpython-314.pyc
    │       │   │   │   │           input_audio_buffer_speech_stopped_event.cpython-314.pyc
    │       │   │   │   │           rate_limits_updated_event.cpython-314.pyc
    │       │   │   │   │           realtime_client_event.cpython-314.pyc
    │       │   │   │   │           realtime_client_event_param.cpython-314.pyc
    │       │   │   │   │           realtime_connect_params.cpython-314.pyc
    │       │   │   │   │           realtime_response.cpython-314.pyc
    │       │   │   │   │           realtime_response_status.cpython-314.pyc
    │       │   │   │   │           realtime_response_usage.cpython-314.pyc
    │       │   │   │   │           realtime_server_event.cpython-314.pyc
    │       │   │   │   │           response_audio_delta_event.cpython-314.pyc
    │       │   │   │   │           response_audio_done_event.cpython-314.pyc
    │       │   │   │   │           response_audio_transcript_delta_event.cpython-314.pyc
    │       │   │   │   │           response_audio_transcript_done_event.cpython-314.pyc
    │       │   │   │   │           response_cancel_event.cpython-314.pyc
    │       │   │   │   │           response_cancel_event_param.cpython-314.pyc
    │       │   │   │   │           response_content_part_added_event.cpython-314.pyc
    │       │   │   │   │           response_content_part_done_event.cpython-314.pyc
    │       │   │   │   │           response_created_event.cpython-314.pyc
    │       │   │   │   │           response_create_event.cpython-314.pyc
    │       │   │   │   │           response_create_event_param.cpython-314.pyc
    │       │   │   │   │           response_done_event.cpython-314.pyc
    │       │   │   │   │           response_function_call_arguments_delta_event.cpython-314.pyc
    │       │   │   │   │           response_function_call_arguments_done_event.cpython-314.pyc
    │       │   │   │   │           response_output_item_added_event.cpython-314.pyc
    │       │   │   │   │           response_output_item_done_event.cpython-314.pyc
    │       │   │   │   │           response_text_delta_event.cpython-314.pyc
    │       │   │   │   │           response_text_done_event.cpython-314.pyc
    │       │   │   │   │           session.cpython-314.pyc
    │       │   │   │   │           session_created_event.cpython-314.pyc
    │       │   │   │   │           session_create_params.cpython-314.pyc
    │       │   │   │   │           session_create_response.cpython-314.pyc
    │       │   │   │   │           session_updated_event.cpython-314.pyc
    │       │   │   │   │           session_update_event.cpython-314.pyc
    │       │   │   │   │           session_update_event_param.cpython-314.pyc
    │       │   │   │   │           transcription_session.cpython-314.pyc
    │       │   │   │   │           transcription_session_create_params.cpython-314.pyc
    │       │   │   │   │           transcription_session_update.cpython-314.pyc
    │       │   │   │   │           transcription_session_updated_event.cpython-314.pyc
    │       │   │   │   │           transcription_session_update_param.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───responses
    │       │   │   │   │   │   beta_response_item_list.py
    │       │   │   │   │   │   input_item_list_params.py
    │       │   │   │   │   │   input_token_count_params.py
    │       │   │   │   │   │   input_token_count_response.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           beta_response_item_list.cpython-314.pyc
    │       │   │   │   │           input_item_list_params.cpython-314.pyc
    │       │   │   │   │           input_token_count_params.cpython-314.pyc
    │       │   │   │   │           input_token_count_response.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───threads
    │       │   │   │   │   │   annotation.py
    │       │   │   │   │   │   annotation_delta.py
    │       │   │   │   │   │   file_citation_annotation.py
    │       │   │   │   │   │   file_citation_delta_annotation.py
    │       │   │   │   │   │   file_path_annotation.py
    │       │   │   │   │   │   file_path_delta_annotation.py
    │       │   │   │   │   │   image_file.py
    │       │   │   │   │   │   image_file_content_block.py
    │       │   │   │   │   │   image_file_content_block_param.py
    │       │   │   │   │   │   image_file_delta.py
    │       │   │   │   │   │   image_file_delta_block.py
    │       │   │   │   │   │   image_file_param.py
    │       │   │   │   │   │   image_url.py
    │       │   │   │   │   │   image_url_content_block.py
    │       │   │   │   │   │   image_url_content_block_param.py
    │       │   │   │   │   │   image_url_delta.py
    │       │   │   │   │   │   image_url_delta_block.py
    │       │   │   │   │   │   image_url_param.py
    │       │   │   │   │   │   message.py
    │       │   │   │   │   │   message_content.py
    │       │   │   │   │   │   message_content_delta.py
    │       │   │   │   │   │   message_content_part_param.py
    │       │   │   │   │   │   message_create_params.py
    │       │   │   │   │   │   message_deleted.py
    │       │   │   │   │   │   message_delta.py
    │       │   │   │   │   │   message_delta_event.py
    │       │   │   │   │   │   message_list_params.py
    │       │   │   │   │   │   message_update_params.py
    │       │   │   │   │   │   refusal_content_block.py
    │       │   │   │   │   │   refusal_delta_block.py
    │       │   │   │   │   │   required_action_function_tool_call.py
    │       │   │   │   │   │   run.py
    │       │   │   │   │   │   run_create_params.py
    │       │   │   │   │   │   run_list_params.py
    │       │   │   │   │   │   run_status.py
    │       │   │   │   │   │   run_submit_tool_outputs_params.py
    │       │   │   │   │   │   run_update_params.py
    │       │   │   │   │   │   text.py
    │       │   │   │   │   │   text_content_block.py
    │       │   │   │   │   │   text_content_block_param.py
    │       │   │   │   │   │   text_delta.py
    │       │   │   │   │   │   text_delta_block.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   ├───runs
    │       │   │   │   │   │   │   code_interpreter_logs.py
    │       │   │   │   │   │   │   code_interpreter_output_image.py
    │       │   │   │   │   │   │   code_interpreter_tool_call.py
    │       │   │   │   │   │   │   code_interpreter_tool_call_delta.py
    │       │   │   │   │   │   │   file_search_tool_call.py
    │       │   │   │   │   │   │   file_search_tool_call_delta.py
    │       │   │   │   │   │   │   function_tool_call.py
    │       │   │   │   │   │   │   function_tool_call_delta.py
    │       │   │   │   │   │   │   message_creation_step_details.py
    │       │   │   │   │   │   │   run_step.py
    │       │   │   │   │   │   │   run_step_delta.py
    │       │   │   │   │   │   │   run_step_delta_event.py
    │       │   │   │   │   │   │   run_step_delta_message_delta.py
    │       │   │   │   │   │   │   run_step_include.py
    │       │   │   │   │   │   │   step_list_params.py
    │       │   │   │   │   │   │   step_retrieve_params.py
    │       │   │   │   │   │   │   tool_call.py
    │       │   │   │   │   │   │   tool_calls_step_details.py
    │       │   │   │   │   │   │   tool_call_delta.py
    │       │   │   │   │   │   │   tool_call_delta_object.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           code_interpreter_logs.cpython-314.pyc
    │       │   │   │   │   │           code_interpreter_output_image.cpython-314.pyc
    │       │   │   │   │   │           code_interpreter_tool_call.cpython-314.pyc
    │       │   │   │   │   │           code_interpreter_tool_call_delta.cpython-314.pyc
    │       │   │   │   │   │           file_search_tool_call.cpython-314.pyc
    │       │   │   │   │   │           file_search_tool_call_delta.cpython-314.pyc
    │       │   │   │   │   │           function_tool_call.cpython-314.pyc
    │       │   │   │   │   │           function_tool_call_delta.cpython-314.pyc
    │       │   │   │   │   │           message_creation_step_details.cpython-314.pyc
    │       │   │   │   │   │           run_step.cpython-314.pyc
    │       │   │   │   │   │           run_step_delta.cpython-314.pyc
    │       │   │   │   │   │           run_step_delta_event.cpython-314.pyc
    │       │   │   │   │   │           run_step_delta_message_delta.cpython-314.pyc
    │       │   │   │   │   │           run_step_include.cpython-314.pyc
    │       │   │   │   │   │           step_list_params.cpython-314.pyc
    │       │   │   │   │   │           step_retrieve_params.cpython-314.pyc
    │       │   │   │   │   │           tool_call.cpython-314.pyc
    │       │   │   │   │   │           tool_calls_step_details.cpython-314.pyc
    │       │   │   │   │   │           tool_call_delta.cpython-314.pyc
    │       │   │   │   │   │           tool_call_delta_object.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           annotation.cpython-314.pyc
    │       │   │   │   │           annotation_delta.cpython-314.pyc
    │       │   │   │   │           file_citation_annotation.cpython-314.pyc
    │       │   │   │   │           file_citation_delta_annotation.cpython-314.pyc
    │       │   │   │   │           file_path_annotation.cpython-314.pyc
    │       │   │   │   │           file_path_delta_annotation.cpython-314.pyc
    │       │   │   │   │           image_file.cpython-314.pyc
    │       │   │   │   │           image_file_content_block.cpython-314.pyc
    │       │   │   │   │           image_file_content_block_param.cpython-314.pyc
    │       │   │   │   │           image_file_delta.cpython-314.pyc
    │       │   │   │   │           image_file_delta_block.cpython-314.pyc
    │       │   │   │   │           image_file_param.cpython-314.pyc
    │       │   │   │   │           image_url.cpython-314.pyc
    │       │   │   │   │           image_url_content_block.cpython-314.pyc
    │       │   │   │   │           image_url_content_block_param.cpython-314.pyc
    │       │   │   │   │           image_url_delta.cpython-314.pyc
    │       │   │   │   │           image_url_delta_block.cpython-314.pyc
    │       │   │   │   │           image_url_param.cpython-314.pyc
    │       │   │   │   │           message.cpython-314.pyc
    │       │   │   │   │           message_content.cpython-314.pyc
    │       │   │   │   │           message_content_delta.cpython-314.pyc
    │       │   │   │   │           message_content_part_param.cpython-314.pyc
    │       │   │   │   │           message_create_params.cpython-314.pyc
    │       │   │   │   │           message_deleted.cpython-314.pyc
    │       │   │   │   │           message_delta.cpython-314.pyc
    │       │   │   │   │           message_delta_event.cpython-314.pyc
    │       │   │   │   │           message_list_params.cpython-314.pyc
    │       │   │   │   │           message_update_params.cpython-314.pyc
    │       │   │   │   │           refusal_content_block.cpython-314.pyc
    │       │   │   │   │           refusal_delta_block.cpython-314.pyc
    │       │   │   │   │           required_action_function_tool_call.cpython-314.pyc
    │       │   │   │   │           run.cpython-314.pyc
    │       │   │   │   │           run_create_params.cpython-314.pyc
    │       │   │   │   │           run_list_params.cpython-314.pyc
    │       │   │   │   │           run_status.cpython-314.pyc
    │       │   │   │   │           run_submit_tool_outputs_params.cpython-314.pyc
    │       │   │   │   │           run_update_params.cpython-314.pyc
    │       │   │   │   │           text.cpython-314.pyc
    │       │   │   │   │           text_content_block.cpython-314.pyc
    │       │   │   │   │           text_content_block_param.cpython-314.pyc
    │       │   │   │   │           text_delta.cpython-314.pyc
    │       │   │   │   │           text_delta_block.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           assistant.cpython-314.pyc
    │       │   │   │           assistant_create_params.cpython-314.pyc
    │       │   │   │           assistant_deleted.cpython-314.pyc
    │       │   │   │           assistant_list_params.cpython-314.pyc
    │       │   │   │           assistant_response_format_option.cpython-314.pyc
    │       │   │   │           assistant_response_format_option_param.cpython-314.pyc
    │       │   │   │           assistant_stream_event.cpython-314.pyc
    │       │   │   │           assistant_tool.cpython-314.pyc
    │       │   │   │           assistant_tool_choice.cpython-314.pyc
    │       │   │   │           assistant_tool_choice_function.cpython-314.pyc
    │       │   │   │           assistant_tool_choice_function_param.cpython-314.pyc
    │       │   │   │           assistant_tool_choice_option.cpython-314.pyc
    │       │   │   │           assistant_tool_choice_option_param.cpython-314.pyc
    │       │   │   │           assistant_tool_choice_param.cpython-314.pyc
    │       │   │   │           assistant_tool_param.cpython-314.pyc
    │       │   │   │           assistant_update_params.cpython-314.pyc
    │       │   │   │           beta_apply_patch_tool.cpython-314.pyc
    │       │   │   │           beta_apply_patch_tool_param.cpython-314.pyc
    │       │   │   │           beta_compacted_response.cpython-314.pyc
    │       │   │   │           beta_computer_action.cpython-314.pyc
    │       │   │   │           beta_computer_action_list.cpython-314.pyc
    │       │   │   │           beta_computer_action_list_param.cpython-314.pyc
    │       │   │   │           beta_computer_action_param.cpython-314.pyc
    │       │   │   │           beta_computer_tool.cpython-314.pyc
    │       │   │   │           beta_computer_tool_param.cpython-314.pyc
    │       │   │   │           beta_computer_use_preview_tool.cpython-314.pyc
    │       │   │   │           beta_computer_use_preview_tool_param.cpython-314.pyc
    │       │   │   │           beta_container_auto.cpython-314.pyc
    │       │   │   │           beta_container_auto_param.cpython-314.pyc
    │       │   │   │           beta_container_network_policy_allowlist.cpython-314.pyc
    │       │   │   │           beta_container_network_policy_allowlist_param.cpython-314.pyc
    │       │   │   │           beta_container_network_policy_disabled.cpython-314.pyc
    │       │   │   │           beta_container_network_policy_disabled_param.cpython-314.pyc
    │       │   │   │           beta_container_network_policy_domain_secret.cpython-314.pyc
    │       │   │   │           beta_container_network_policy_domain_secret_param.cpython-314.pyc
    │       │   │   │           beta_container_reference.cpython-314.pyc
    │       │   │   │           beta_container_reference_param.cpython-314.pyc
    │       │   │   │           beta_custom_tool.cpython-314.pyc
    │       │   │   │           beta_custom_tool_param.cpython-314.pyc
    │       │   │   │           beta_easy_input_message.cpython-314.pyc
    │       │   │   │           beta_easy_input_message_param.cpython-314.pyc
    │       │   │   │           beta_file_search_tool.cpython-314.pyc
    │       │   │   │           beta_file_search_tool_param.cpython-314.pyc
    │       │   │   │           beta_function_shell_tool.cpython-314.pyc
    │       │   │   │           beta_function_shell_tool_param.cpython-314.pyc
    │       │   │   │           beta_function_tool.cpython-314.pyc
    │       │   │   │           beta_function_tool_param.cpython-314.pyc
    │       │   │   │           beta_inline_skill.cpython-314.pyc
    │       │   │   │           beta_inline_skill_param.cpython-314.pyc
    │       │   │   │           beta_inline_skill_source.cpython-314.pyc
    │       │   │   │           beta_inline_skill_source_param.cpython-314.pyc
    │       │   │   │           beta_local_environment.cpython-314.pyc
    │       │   │   │           beta_local_environment_param.cpython-314.pyc
    │       │   │   │           beta_local_skill.cpython-314.pyc
    │       │   │   │           beta_local_skill_param.cpython-314.pyc
    │       │   │   │           beta_namespace_tool.cpython-314.pyc
    │       │   │   │           beta_namespace_tool_param.cpython-314.pyc
    │       │   │   │           beta_response.cpython-314.pyc
    │       │   │   │           beta_responses_client_event.cpython-314.pyc
    │       │   │   │           beta_responses_client_event_param.cpython-314.pyc
    │       │   │   │           beta_responses_server_event.cpython-314.pyc
    │       │   │   │           beta_response_apply_patch_tool_call.cpython-314.pyc
    │       │   │   │           beta_response_apply_patch_tool_call_output.cpython-314.pyc
    │       │   │   │           beta_response_audio_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_audio_done_event.cpython-314.pyc
    │       │   │   │           beta_response_audio_transcript_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_audio_transcript_done_event.cpython-314.pyc
    │       │   │   │           beta_response_code_interpreter_call_code_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_code_interpreter_call_code_done_event.cpython-314.pyc
    │       │   │   │           beta_response_code_interpreter_call_completed_event.cpython-314.pyc
    │       │   │   │           beta_response_code_interpreter_call_interpreting_event.cpython-314.pyc
    │       │   │   │           beta_response_code_interpreter_call_in_progress_event.cpython-314.pyc
    │       │   │   │           beta_response_code_interpreter_tool_call.cpython-314.pyc
    │       │   │   │           beta_response_code_interpreter_tool_call_param.cpython-314.pyc
    │       │   │   │           beta_response_compaction_item.cpython-314.pyc
    │       │   │   │           beta_response_compaction_item_param.cpython-314.pyc
    │       │   │   │           beta_response_compaction_item_param_param.cpython-314.pyc
    │       │   │   │           beta_response_completed_event.cpython-314.pyc
    │       │   │   │           beta_response_computer_tool_call.cpython-314.pyc
    │       │   │   │           beta_response_computer_tool_call_output_item.cpython-314.pyc
    │       │   │   │           beta_response_computer_tool_call_output_screenshot.cpython-314.pyc
    │       │   │   │           beta_response_computer_tool_call_output_screenshot_param.cpython-314.pyc
    │       │   │   │           beta_response_computer_tool_call_param.cpython-314.pyc
    │       │   │   │           beta_response_container_reference.cpython-314.pyc
    │       │   │   │           beta_response_content_part_added_event.cpython-314.pyc
    │       │   │   │           beta_response_content_part_done_event.cpython-314.pyc
    │       │   │   │           beta_response_conversation_param.cpython-314.pyc
    │       │   │   │           beta_response_conversation_param_param.cpython-314.pyc
    │       │   │   │           beta_response_created_event.cpython-314.pyc
    │       │   │   │           beta_response_custom_tool_call.cpython-314.pyc
    │       │   │   │           beta_response_custom_tool_call_input_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_custom_tool_call_input_done_event.cpython-314.pyc
    │       │   │   │           beta_response_custom_tool_call_item.cpython-314.pyc
    │       │   │   │           beta_response_custom_tool_call_output.cpython-314.pyc
    │       │   │   │           beta_response_custom_tool_call_output_item.cpython-314.pyc
    │       │   │   │           beta_response_custom_tool_call_output_param.cpython-314.pyc
    │       │   │   │           beta_response_custom_tool_call_param.cpython-314.pyc
    │       │   │   │           beta_response_error.cpython-314.pyc
    │       │   │   │           beta_response_error_event.cpython-314.pyc
    │       │   │   │           beta_response_failed_event.cpython-314.pyc
    │       │   │   │           beta_response_file_search_call_completed_event.cpython-314.pyc
    │       │   │   │           beta_response_file_search_call_in_progress_event.cpython-314.pyc
    │       │   │   │           beta_response_file_search_call_searching_event.cpython-314.pyc
    │       │   │   │           beta_response_file_search_tool_call.cpython-314.pyc
    │       │   │   │           beta_response_file_search_tool_call_param.cpython-314.pyc
    │       │   │   │           beta_response_format_text_config.cpython-314.pyc
    │       │   │   │           beta_response_format_text_config_param.cpython-314.pyc
    │       │   │   │           beta_response_format_text_json_schema_config.cpython-314.pyc
    │       │   │   │           beta_response_format_text_json_schema_config_param.cpython-314.pyc
    │       │   │   │           beta_response_function_call_arguments_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_function_call_arguments_done_event.cpython-314.pyc
    │       │   │   │           beta_response_function_call_output_item.cpython-314.pyc
    │       │   │   │           beta_response_function_call_output_item_list.cpython-314.pyc
    │       │   │   │           beta_response_function_call_output_item_list_param.cpython-314.pyc
    │       │   │   │           beta_response_function_call_output_item_param.cpython-314.pyc
    │       │   │   │           beta_response_function_shell_call_output_content.cpython-314.pyc
    │       │   │   │           beta_response_function_shell_call_output_content_param.cpython-314.pyc
    │       │   │   │           beta_response_function_shell_tool_call.cpython-314.pyc
    │       │   │   │           beta_response_function_shell_tool_call_output.cpython-314.pyc
    │       │   │   │           beta_response_function_tool_call.cpython-314.pyc
    │       │   │   │           beta_response_function_tool_call_item.cpython-314.pyc
    │       │   │   │           beta_response_function_tool_call_output_item.cpython-314.pyc
    │       │   │   │           beta_response_function_tool_call_param.cpython-314.pyc
    │       │   │   │           beta_response_function_web_search.cpython-314.pyc
    │       │   │   │           beta_response_function_web_search_param.cpython-314.pyc
    │       │   │   │           beta_response_image_gen_call_completed_event.cpython-314.pyc
    │       │   │   │           beta_response_image_gen_call_generating_event.cpython-314.pyc
    │       │   │   │           beta_response_image_gen_call_in_progress_event.cpython-314.pyc
    │       │   │   │           beta_response_image_gen_call_partial_image_event.cpython-314.pyc
    │       │   │   │           beta_response_includable.cpython-314.pyc
    │       │   │   │           beta_response_incomplete_event.cpython-314.pyc
    │       │   │   │           beta_response_inject_created_event.cpython-314.pyc
    │       │   │   │           beta_response_inject_event.cpython-314.pyc
    │       │   │   │           beta_response_inject_event_param.cpython-314.pyc
    │       │   │   │           beta_response_inject_failed_event.cpython-314.pyc
    │       │   │   │           beta_response_input.cpython-314.pyc
    │       │   │   │           beta_response_input_content.cpython-314.pyc
    │       │   │   │           beta_response_input_content_param.cpython-314.pyc
    │       │   │   │           beta_response_input_file.cpython-314.pyc
    │       │   │   │           beta_response_input_file_content.cpython-314.pyc
    │       │   │   │           beta_response_input_file_content_param.cpython-314.pyc
    │       │   │   │           beta_response_input_file_param.cpython-314.pyc
    │       │   │   │           beta_response_input_image.cpython-314.pyc
    │       │   │   │           beta_response_input_image_content.cpython-314.pyc
    │       │   │   │           beta_response_input_image_content_param.cpython-314.pyc
    │       │   │   │           beta_response_input_image_param.cpython-314.pyc
    │       │   │   │           beta_response_input_item.cpython-314.pyc
    │       │   │   │           beta_response_input_item_param.cpython-314.pyc
    │       │   │   │           beta_response_input_message_content_list.cpython-314.pyc
    │       │   │   │           beta_response_input_message_content_list_param.cpython-314.pyc
    │       │   │   │           beta_response_input_message_item.cpython-314.pyc
    │       │   │   │           beta_response_input_param.cpython-314.pyc
    │       │   │   │           beta_response_input_text.cpython-314.pyc
    │       │   │   │           beta_response_input_text_content.cpython-314.pyc
    │       │   │   │           beta_response_input_text_content_param.cpython-314.pyc
    │       │   │   │           beta_response_input_text_param.cpython-314.pyc
    │       │   │   │           beta_response_in_progress_event.cpython-314.pyc
    │       │   │   │           beta_response_item.cpython-314.pyc
    │       │   │   │           beta_response_local_environment.cpython-314.pyc
    │       │   │   │           beta_response_mcp_call_arguments_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_mcp_call_arguments_done_event.cpython-314.pyc
    │       │   │   │           beta_response_mcp_call_completed_event.cpython-314.pyc
    │       │   │   │           beta_response_mcp_call_failed_event.cpython-314.pyc
    │       │   │   │           beta_response_mcp_call_in_progress_event.cpython-314.pyc
    │       │   │   │           beta_response_mcp_list_tools_completed_event.cpython-314.pyc
    │       │   │   │           beta_response_mcp_list_tools_failed_event.cpython-314.pyc
    │       │   │   │           beta_response_mcp_list_tools_in_progress_event.cpython-314.pyc
    │       │   │   │           beta_response_output_item.cpython-314.pyc
    │       │   │   │           beta_response_output_item_added_event.cpython-314.pyc
    │       │   │   │           beta_response_output_item_done_event.cpython-314.pyc
    │       │   │   │           beta_response_output_message.cpython-314.pyc
    │       │   │   │           beta_response_output_message_param.cpython-314.pyc
    │       │   │   │           beta_response_output_refusal.cpython-314.pyc
    │       │   │   │           beta_response_output_refusal_param.cpython-314.pyc
    │       │   │   │           beta_response_output_text.cpython-314.pyc
    │       │   │   │           beta_response_output_text_annotation_added_event.cpython-314.pyc
    │       │   │   │           beta_response_output_text_param.cpython-314.pyc
    │       │   │   │           beta_response_prompt.cpython-314.pyc
    │       │   │   │           beta_response_prompt_param.cpython-314.pyc
    │       │   │   │           beta_response_queued_event.cpython-314.pyc
    │       │   │   │           beta_response_reasoning_item.cpython-314.pyc
    │       │   │   │           beta_response_reasoning_item_param.cpython-314.pyc
    │       │   │   │           beta_response_reasoning_summary_part_added_event.cpython-314.pyc
    │       │   │   │           beta_response_reasoning_summary_part_done_event.cpython-314.pyc
    │       │   │   │           beta_response_reasoning_summary_text_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_reasoning_summary_text_done_event.cpython-314.pyc
    │       │   │   │           beta_response_reasoning_text_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_reasoning_text_done_event.cpython-314.pyc
    │       │   │   │           beta_response_refusal_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_refusal_done_event.cpython-314.pyc
    │       │   │   │           beta_response_status.cpython-314.pyc
    │       │   │   │           beta_response_stream_event.cpython-314.pyc
    │       │   │   │           beta_response_text_config.cpython-314.pyc
    │       │   │   │           beta_response_text_config_param.cpython-314.pyc
    │       │   │   │           beta_response_text_delta_event.cpython-314.pyc
    │       │   │   │           beta_response_text_done_event.cpython-314.pyc
    │       │   │   │           beta_response_tool_search_call.cpython-314.pyc
    │       │   │   │           beta_response_tool_search_output_item.cpython-314.pyc
    │       │   │   │           beta_response_tool_search_output_item_param.cpython-314.pyc
    │       │   │   │           beta_response_tool_search_output_item_param_param.cpython-314.pyc
    │       │   │   │           beta_response_usage.cpython-314.pyc
    │       │   │   │           beta_response_web_search_call_completed_event.cpython-314.pyc
    │       │   │   │           beta_response_web_search_call_in_progress_event.cpython-314.pyc
    │       │   │   │           beta_response_web_search_call_searching_event.cpython-314.pyc
    │       │   │   │           beta_skill_reference.cpython-314.pyc
    │       │   │   │           beta_skill_reference_param.cpython-314.pyc
    │       │   │   │           beta_tool.cpython-314.pyc
    │       │   │   │           beta_tool_choice_allowed.cpython-314.pyc
    │       │   │   │           beta_tool_choice_allowed_param.cpython-314.pyc
    │       │   │   │           beta_tool_choice_apply_patch.cpython-314.pyc
    │       │   │   │           beta_tool_choice_apply_patch_param.cpython-314.pyc
    │       │   │   │           beta_tool_choice_custom.cpython-314.pyc
    │       │   │   │           beta_tool_choice_custom_param.cpython-314.pyc
    │       │   │   │           beta_tool_choice_function.cpython-314.pyc
    │       │   │   │           beta_tool_choice_function_param.cpython-314.pyc
    │       │   │   │           beta_tool_choice_mcp.cpython-314.pyc
    │       │   │   │           beta_tool_choice_mcp_param.cpython-314.pyc
    │       │   │   │           beta_tool_choice_options.cpython-314.pyc
    │       │   │   │           beta_tool_choice_shell.cpython-314.pyc
    │       │   │   │           beta_tool_choice_shell_param.cpython-314.pyc
    │       │   │   │           beta_tool_choice_types.cpython-314.pyc
    │       │   │   │           beta_tool_choice_types_param.cpython-314.pyc
    │       │   │   │           beta_tool_param.cpython-314.pyc
    │       │   │   │           beta_tool_search_tool.cpython-314.pyc
    │       │   │   │           beta_tool_search_tool_param.cpython-314.pyc
    │       │   │   │           beta_web_search_preview_tool.cpython-314.pyc
    │       │   │   │           beta_web_search_preview_tool_param.cpython-314.pyc
    │       │   │   │           beta_web_search_tool.cpython-314.pyc
    │       │   │   │           beta_web_search_tool_param.cpython-314.pyc
    │       │   │   │           chatkit_workflow.cpython-314.pyc
    │       │   │   │           code_interpreter_tool.cpython-314.pyc
    │       │   │   │           code_interpreter_tool_param.cpython-314.pyc
    │       │   │   │           file_search_tool.cpython-314.pyc
    │       │   │   │           file_search_tool_param.cpython-314.pyc
    │       │   │   │           function_tool.cpython-314.pyc
    │       │   │   │           function_tool_param.cpython-314.pyc
    │       │   │   │           response_compact_params.cpython-314.pyc
    │       │   │   │           response_create_params.cpython-314.pyc
    │       │   │   │           response_retrieve_params.cpython-314.pyc
    │       │   │   │           thread.cpython-314.pyc
    │       │   │   │           thread_create_and_run_params.cpython-314.pyc
    │       │   │   │           thread_create_params.cpython-314.pyc
    │       │   │   │           thread_deleted.cpython-314.pyc
    │       │   │   │           thread_update_params.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───chat
    │       │   │   │   │   chat_completion.py
    │       │   │   │   │   chat_completion_allowed_tools_param.py
    │       │   │   │   │   chat_completion_allowed_tool_choice_param.py
    │       │   │   │   │   chat_completion_assistant_message_param.py
    │       │   │   │   │   chat_completion_audio.py
    │       │   │   │   │   chat_completion_audio_param.py
    │       │   │   │   │   chat_completion_chunk.py
    │       │   │   │   │   chat_completion_content_part_image.py
    │       │   │   │   │   chat_completion_content_part_image_param.py
    │       │   │   │   │   chat_completion_content_part_input_audio_param.py
    │       │   │   │   │   chat_completion_content_part_param.py
    │       │   │   │   │   chat_completion_content_part_refusal_param.py
    │       │   │   │   │   chat_completion_content_part_text.py
    │       │   │   │   │   chat_completion_content_part_text_param.py
    │       │   │   │   │   chat_completion_custom_tool_param.py
    │       │   │   │   │   chat_completion_deleted.py
    │       │   │   │   │   chat_completion_developer_message_param.py
    │       │   │   │   │   chat_completion_function_call_option_param.py
    │       │   │   │   │   chat_completion_function_message_param.py
    │       │   │   │   │   chat_completion_function_tool.py
    │       │   │   │   │   chat_completion_function_tool_param.py
    │       │   │   │   │   chat_completion_message.py
    │       │   │   │   │   chat_completion_message_custom_tool_call.py
    │       │   │   │   │   chat_completion_message_custom_tool_call_param.py
    │       │   │   │   │   chat_completion_message_function_tool_call.py
    │       │   │   │   │   chat_completion_message_function_tool_call_param.py
    │       │   │   │   │   chat_completion_message_param.py
    │       │   │   │   │   chat_completion_message_tool_call.py
    │       │   │   │   │   chat_completion_message_tool_call_param.py
    │       │   │   │   │   chat_completion_message_tool_call_union_param.py
    │       │   │   │   │   chat_completion_modality.py
    │       │   │   │   │   chat_completion_named_tool_choice_custom_param.py
    │       │   │   │   │   chat_completion_named_tool_choice_param.py
    │       │   │   │   │   chat_completion_prediction_content_param.py
    │       │   │   │   │   chat_completion_reasoning_effort.py
    │       │   │   │   │   chat_completion_role.py
    │       │   │   │   │   chat_completion_store_message.py
    │       │   │   │   │   chat_completion_stream_options_param.py
    │       │   │   │   │   chat_completion_system_message_param.py
    │       │   │   │   │   chat_completion_token_logprob.py
    │       │   │   │   │   chat_completion_tool_choice_option_param.py
    │       │   │   │   │   chat_completion_tool_message_param.py
    │       │   │   │   │   chat_completion_tool_param.py
    │       │   │   │   │   chat_completion_tool_union_param.py
    │       │   │   │   │   chat_completion_user_message_param.py
    │       │   │   │   │   completion_create_params.py
    │       │   │   │   │   completion_list_params.py
    │       │   │   │   │   completion_update_params.py
    │       │   │   │   │   parsed_chat_completion.py
    │       │   │   │   │   parsed_function_tool_call.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───completions
    │       │   │   │   │   │   message_list_params.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           message_list_params.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           chat_completion.cpython-314.pyc
    │       │   │   │           chat_completion_allowed_tools_param.cpython-314.pyc
    │       │   │   │           chat_completion_allowed_tool_choice_param.cpython-314.pyc
    │       │   │   │           chat_completion_assistant_message_param.cpython-314.pyc
    │       │   │   │           chat_completion_audio.cpython-314.pyc
    │       │   │   │           chat_completion_audio_param.cpython-314.pyc
    │       │   │   │           chat_completion_chunk.cpython-314.pyc
    │       │   │   │           chat_completion_content_part_image.cpython-314.pyc
    │       │   │   │           chat_completion_content_part_image_param.cpython-314.pyc
    │       │   │   │           chat_completion_content_part_input_audio_param.cpython-314.pyc
    │       │   │   │           chat_completion_content_part_param.cpython-314.pyc
    │       │   │   │           chat_completion_content_part_refusal_param.cpython-314.pyc
    │       │   │   │           chat_completion_content_part_text.cpython-314.pyc
    │       │   │   │           chat_completion_content_part_text_param.cpython-314.pyc
    │       │   │   │           chat_completion_custom_tool_param.cpython-314.pyc
    │       │   │   │           chat_completion_deleted.cpython-314.pyc
    │       │   │   │           chat_completion_developer_message_param.cpython-314.pyc
    │       │   │   │           chat_completion_function_call_option_param.cpython-314.pyc
    │       │   │   │           chat_completion_function_message_param.cpython-314.pyc
    │       │   │   │           chat_completion_function_tool.cpython-314.pyc
    │       │   │   │           chat_completion_function_tool_param.cpython-314.pyc
    │       │   │   │           chat_completion_message.cpython-314.pyc
    │       │   │   │           chat_completion_message_custom_tool_call.cpython-314.pyc
    │       │   │   │           chat_completion_message_custom_tool_call_param.cpython-314.pyc
    │       │   │   │           chat_completion_message_function_tool_call.cpython-314.pyc
    │       │   │   │           chat_completion_message_function_tool_call_param.cpython-314.pyc
    │       │   │   │           chat_completion_message_param.cpython-314.pyc
    │       │   │   │           chat_completion_message_tool_call.cpython-314.pyc
    │       │   │   │           chat_completion_message_tool_call_param.cpython-314.pyc
    │       │   │   │           chat_completion_message_tool_call_union_param.cpython-314.pyc
    │       │   │   │           chat_completion_modality.cpython-314.pyc
    │       │   │   │           chat_completion_named_tool_choice_custom_param.cpython-314.pyc
    │       │   │   │           chat_completion_named_tool_choice_param.cpython-314.pyc
    │       │   │   │           chat_completion_prediction_content_param.cpython-314.pyc
    │       │   │   │           chat_completion_reasoning_effort.cpython-314.pyc
    │       │   │   │           chat_completion_role.cpython-314.pyc
    │       │   │   │           chat_completion_store_message.cpython-314.pyc
    │       │   │   │           chat_completion_stream_options_param.cpython-314.pyc
    │       │   │   │           chat_completion_system_message_param.cpython-314.pyc
    │       │   │   │           chat_completion_token_logprob.cpython-314.pyc
    │       │   │   │           chat_completion_tool_choice_option_param.cpython-314.pyc
    │       │   │   │           chat_completion_tool_message_param.cpython-314.pyc
    │       │   │   │           chat_completion_tool_param.cpython-314.pyc
    │       │   │   │           chat_completion_tool_union_param.cpython-314.pyc
    │       │   │   │           chat_completion_user_message_param.cpython-314.pyc
    │       │   │   │           completion_create_params.cpython-314.pyc
    │       │   │   │           completion_list_params.cpython-314.pyc
    │       │   │   │           completion_update_params.cpython-314.pyc
    │       │   │   │           parsed_chat_completion.cpython-314.pyc
    │       │   │   │           parsed_function_tool_call.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───containers
    │       │   │   │   │   file_create_params.py
    │       │   │   │   │   file_create_response.py
    │       │   │   │   │   file_list_params.py
    │       │   │   │   │   file_list_response.py
    │       │   │   │   │   file_retrieve_response.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───files
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           file_create_params.cpython-314.pyc
    │       │   │   │           file_create_response.cpython-314.pyc
    │       │   │   │           file_list_params.cpython-314.pyc
    │       │   │   │           file_list_response.cpython-314.pyc
    │       │   │   │           file_retrieve_response.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───conversations
    │       │   │   │   │   computer_screenshot_content.py
    │       │   │   │   │   conversation.py
    │       │   │   │   │   conversation_create_params.py
    │       │   │   │   │   conversation_deleted_resource.py
    │       │   │   │   │   conversation_item.py
    │       │   │   │   │   conversation_item_list.py
    │       │   │   │   │   conversation_update_params.py
    │       │   │   │   │   input_file_content.py
    │       │   │   │   │   input_file_content_param.py
    │       │   │   │   │   input_image_content.py
    │       │   │   │   │   input_image_content_param.py
    │       │   │   │   │   input_text_content.py
    │       │   │   │   │   input_text_content_param.py
    │       │   │   │   │   item_create_params.py
    │       │   │   │   │   item_list_params.py
    │       │   │   │   │   item_retrieve_params.py
    │       │   │   │   │   message.py
    │       │   │   │   │   output_text_content.py
    │       │   │   │   │   output_text_content_param.py
    │       │   │   │   │   refusal_content.py
    │       │   │   │   │   refusal_content_param.py
    │       │   │   │   │   summary_text_content.py
    │       │   │   │   │   text_content.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           computer_screenshot_content.cpython-314.pyc
    │       │   │   │           conversation.cpython-314.pyc
    │       │   │   │           conversation_create_params.cpython-314.pyc
    │       │   │   │           conversation_deleted_resource.cpython-314.pyc
    │       │   │   │           conversation_item.cpython-314.pyc
    │       │   │   │           conversation_item_list.cpython-314.pyc
    │       │   │   │           conversation_update_params.cpython-314.pyc
    │       │   │   │           input_file_content.cpython-314.pyc
    │       │   │   │           input_file_content_param.cpython-314.pyc
    │       │   │   │           input_image_content.cpython-314.pyc
    │       │   │   │           input_image_content_param.cpython-314.pyc
    │       │   │   │           input_text_content.cpython-314.pyc
    │       │   │   │           input_text_content_param.cpython-314.pyc
    │       │   │   │           item_create_params.cpython-314.pyc
    │       │   │   │           item_list_params.cpython-314.pyc
    │       │   │   │           item_retrieve_params.cpython-314.pyc
    │       │   │   │           message.cpython-314.pyc
    │       │   │   │           output_text_content.cpython-314.pyc
    │       │   │   │           output_text_content_param.cpython-314.pyc
    │       │   │   │           refusal_content.cpython-314.pyc
    │       │   │   │           refusal_content_param.cpython-314.pyc
    │       │   │   │           summary_text_content.cpython-314.pyc
    │       │   │   │           text_content.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───evals
    │       │   │   │   │   create_eval_completions_run_data_source.py
    │       │   │   │   │   create_eval_completions_run_data_source_param.py
    │       │   │   │   │   create_eval_jsonl_run_data_source.py
    │       │   │   │   │   create_eval_jsonl_run_data_source_param.py
    │       │   │   │   │   eval_api_error.py
    │       │   │   │   │   run_cancel_response.py
    │       │   │   │   │   run_create_params.py
    │       │   │   │   │   run_create_response.py
    │       │   │   │   │   run_delete_response.py
    │       │   │   │   │   run_list_params.py
    │       │   │   │   │   run_list_response.py
    │       │   │   │   │   run_retrieve_response.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───runs
    │       │   │   │   │   │   output_item_list_params.py
    │       │   │   │   │   │   output_item_list_response.py
    │       │   │   │   │   │   output_item_retrieve_response.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           output_item_list_params.cpython-314.pyc
    │       │   │   │   │           output_item_list_response.cpython-314.pyc
    │       │   │   │   │           output_item_retrieve_response.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           create_eval_completions_run_data_source.cpython-314.pyc
    │       │   │   │           create_eval_completions_run_data_source_param.cpython-314.pyc
    │       │   │   │           create_eval_jsonl_run_data_source.cpython-314.pyc
    │       │   │   │           create_eval_jsonl_run_data_source_param.cpython-314.pyc
    │       │   │   │           eval_api_error.cpython-314.pyc
    │       │   │   │           run_cancel_response.cpython-314.pyc
    │       │   │   │           run_create_params.cpython-314.pyc
    │       │   │   │           run_create_response.cpython-314.pyc
    │       │   │   │           run_delete_response.cpython-314.pyc
    │       │   │   │           run_list_params.cpython-314.pyc
    │       │   │   │           run_list_response.cpython-314.pyc
    │       │   │   │           run_retrieve_response.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───fine_tuning
    │       │   │   │   │   dpo_hyperparameters.py
    │       │   │   │   │   dpo_hyperparameters_param.py
    │       │   │   │   │   dpo_method.py
    │       │   │   │   │   dpo_method_param.py
    │       │   │   │   │   fine_tuning_job.py
    │       │   │   │   │   fine_tuning_job_event.py
    │       │   │   │   │   fine_tuning_job_integration.py
    │       │   │   │   │   fine_tuning_job_wandb_integration.py
    │       │   │   │   │   fine_tuning_job_wandb_integration_object.py
    │       │   │   │   │   job_create_params.py
    │       │   │   │   │   job_list_events_params.py
    │       │   │   │   │   job_list_params.py
    │       │   │   │   │   reinforcement_hyperparameters.py
    │       │   │   │   │   reinforcement_hyperparameters_param.py
    │       │   │   │   │   reinforcement_method.py
    │       │   │   │   │   reinforcement_method_param.py
    │       │   │   │   │   supervised_hyperparameters.py
    │       │   │   │   │   supervised_hyperparameters_param.py
    │       │   │   │   │   supervised_method.py
    │       │   │   │   │   supervised_method_param.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───alpha
    │       │   │   │   │   │   grader_run_params.py
    │       │   │   │   │   │   grader_run_response.py
    │       │   │   │   │   │   grader_validate_params.py
    │       │   │   │   │   │   grader_validate_response.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           grader_run_params.cpython-314.pyc
    │       │   │   │   │           grader_run_response.cpython-314.pyc
    │       │   │   │   │           grader_validate_params.cpython-314.pyc
    │       │   │   │   │           grader_validate_response.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───checkpoints
    │       │   │   │   │   │   permission_create_params.py
    │       │   │   │   │   │   permission_create_response.py
    │       │   │   │   │   │   permission_delete_response.py
    │       │   │   │   │   │   permission_list_params.py
    │       │   │   │   │   │   permission_list_response.py
    │       │   │   │   │   │   permission_retrieve_params.py
    │       │   │   │   │   │   permission_retrieve_response.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           permission_create_params.cpython-314.pyc
    │       │   │   │   │           permission_create_response.cpython-314.pyc
    │       │   │   │   │           permission_delete_response.cpython-314.pyc
    │       │   │   │   │           permission_list_params.cpython-314.pyc
    │       │   │   │   │           permission_list_response.cpython-314.pyc
    │       │   │   │   │           permission_retrieve_params.cpython-314.pyc
    │       │   │   │   │           permission_retrieve_response.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───jobs
    │       │   │   │   │   │   checkpoint_list_params.py
    │       │   │   │   │   │   fine_tuning_job_checkpoint.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           checkpoint_list_params.cpython-314.pyc
    │       │   │   │   │           fine_tuning_job_checkpoint.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           dpo_hyperparameters.cpython-314.pyc
    │       │   │   │           dpo_hyperparameters_param.cpython-314.pyc
    │       │   │   │           dpo_method.cpython-314.pyc
    │       │   │   │           dpo_method_param.cpython-314.pyc
    │       │   │   │           fine_tuning_job.cpython-314.pyc
    │       │   │   │           fine_tuning_job_event.cpython-314.pyc
    │       │   │   │           fine_tuning_job_integration.cpython-314.pyc
    │       │   │   │           fine_tuning_job_wandb_integration.cpython-314.pyc
    │       │   │   │           fine_tuning_job_wandb_integration_object.cpython-314.pyc
    │       │   │   │           job_create_params.cpython-314.pyc
    │       │   │   │           job_list_events_params.cpython-314.pyc
    │       │   │   │           job_list_params.cpython-314.pyc
    │       │   │   │           reinforcement_hyperparameters.cpython-314.pyc
    │       │   │   │           reinforcement_hyperparameters_param.cpython-314.pyc
    │       │   │   │           reinforcement_method.cpython-314.pyc
    │       │   │   │           reinforcement_method_param.cpython-314.pyc
    │       │   │   │           supervised_hyperparameters.cpython-314.pyc
    │       │   │   │           supervised_hyperparameters_param.cpython-314.pyc
    │       │   │   │           supervised_method.cpython-314.pyc
    │       │   │   │           supervised_method_param.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───graders
    │       │   │   │   │   grader_inputs.py
    │       │   │   │   │   grader_inputs_param.py
    │       │   │   │   │   label_model_grader.py
    │       │   │   │   │   label_model_grader_param.py
    │       │   │   │   │   multi_grader.py
    │       │   │   │   │   multi_grader_param.py
    │       │   │   │   │   python_grader.py
    │       │   │   │   │   python_grader_param.py
    │       │   │   │   │   score_model_grader.py
    │       │   │   │   │   score_model_grader_param.py
    │       │   │   │   │   string_check_grader.py
    │       │   │   │   │   string_check_grader_param.py
    │       │   │   │   │   text_similarity_grader.py
    │       │   │   │   │   text_similarity_grader_param.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           grader_inputs.cpython-314.pyc
    │       │   │   │           grader_inputs_param.cpython-314.pyc
    │       │   │   │           label_model_grader.cpython-314.pyc
    │       │   │   │           label_model_grader_param.cpython-314.pyc
    │       │   │   │           multi_grader.cpython-314.pyc
    │       │   │   │           multi_grader_param.cpython-314.pyc
    │       │   │   │           python_grader.cpython-314.pyc
    │       │   │   │           python_grader_param.cpython-314.pyc
    │       │   │   │           score_model_grader.cpython-314.pyc
    │       │   │   │           score_model_grader_param.cpython-314.pyc
    │       │   │   │           string_check_grader.cpython-314.pyc
    │       │   │   │           string_check_grader_param.cpython-314.pyc
    │       │   │   │           text_similarity_grader.cpython-314.pyc
    │       │   │   │           text_similarity_grader_param.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───realtime
    │       │   │   │   │   audio_transcription.py
    │       │   │   │   │   audio_transcription_param.py
    │       │   │   │   │   call_accept_params.py
    │       │   │   │   │   call_create_params.py
    │       │   │   │   │   call_refer_params.py
    │       │   │   │   │   call_reject_params.py
    │       │   │   │   │   client_secret_create_params.py
    │       │   │   │   │   client_secret_create_response.py
    │       │   │   │   │   conversation_created_event.py
    │       │   │   │   │   conversation_item.py
    │       │   │   │   │   conversation_item_added.py
    │       │   │   │   │   conversation_item_created_event.py
    │       │   │   │   │   conversation_item_create_event.py
    │       │   │   │   │   conversation_item_create_event_param.py
    │       │   │   │   │   conversation_item_deleted_event.py
    │       │   │   │   │   conversation_item_delete_event.py
    │       │   │   │   │   conversation_item_delete_event_param.py
    │       │   │   │   │   conversation_item_done.py
    │       │   │   │   │   conversation_item_input_audio_transcription_completed_event.py
    │       │   │   │   │   conversation_item_input_audio_transcription_delta_event.py
    │       │   │   │   │   conversation_item_input_audio_transcription_failed_event.py
    │       │   │   │   │   conversation_item_input_audio_transcription_segment.py
    │       │   │   │   │   conversation_item_param.py
    │       │   │   │   │   conversation_item_retrieve_event.py
    │       │   │   │   │   conversation_item_retrieve_event_param.py
    │       │   │   │   │   conversation_item_truncated_event.py
    │       │   │   │   │   conversation_item_truncate_event.py
    │       │   │   │   │   conversation_item_truncate_event_param.py
    │       │   │   │   │   input_audio_buffer_append_event.py
    │       │   │   │   │   input_audio_buffer_append_event_param.py
    │       │   │   │   │   input_audio_buffer_cleared_event.py
    │       │   │   │   │   input_audio_buffer_clear_event.py
    │       │   │   │   │   input_audio_buffer_clear_event_param.py
    │       │   │   │   │   input_audio_buffer_committed_event.py
    │       │   │   │   │   input_audio_buffer_commit_event.py
    │       │   │   │   │   input_audio_buffer_commit_event_param.py
    │       │   │   │   │   input_audio_buffer_dtmf_event_received_event.py
    │       │   │   │   │   input_audio_buffer_speech_started_event.py
    │       │   │   │   │   input_audio_buffer_speech_stopped_event.py
    │       │   │   │   │   input_audio_buffer_timeout_triggered.py
    │       │   │   │   │   log_prob_properties.py
    │       │   │   │   │   mcp_list_tools_completed.py
    │       │   │   │   │   mcp_list_tools_failed.py
    │       │   │   │   │   mcp_list_tools_in_progress.py
    │       │   │   │   │   noise_reduction_type.py
    │       │   │   │   │   output_audio_buffer_clear_event.py
    │       │   │   │   │   output_audio_buffer_clear_event_param.py
    │       │   │   │   │   rate_limits_updated_event.py
    │       │   │   │   │   realtime_audio_config.py
    │       │   │   │   │   realtime_audio_config_input.py
    │       │   │   │   │   realtime_audio_config_input_param.py
    │       │   │   │   │   realtime_audio_config_output.py
    │       │   │   │   │   realtime_audio_config_output_param.py
    │       │   │   │   │   realtime_audio_config_param.py
    │       │   │   │   │   realtime_audio_formats.py
    │       │   │   │   │   realtime_audio_formats_param.py
    │       │   │   │   │   realtime_audio_input_turn_detection.py
    │       │   │   │   │   realtime_audio_input_turn_detection_param.py
    │       │   │   │   │   realtime_client_event.py
    │       │   │   │   │   realtime_client_event_param.py
    │       │   │   │   │   realtime_connect_params.py
    │       │   │   │   │   realtime_conversation_item_assistant_message.py
    │       │   │   │   │   realtime_conversation_item_assistant_message_param.py
    │       │   │   │   │   realtime_conversation_item_function_call.py
    │       │   │   │   │   realtime_conversation_item_function_call_output.py
    │       │   │   │   │   realtime_conversation_item_function_call_output_param.py
    │       │   │   │   │   realtime_conversation_item_function_call_param.py
    │       │   │   │   │   realtime_conversation_item_system_message.py
    │       │   │   │   │   realtime_conversation_item_system_message_param.py
    │       │   │   │   │   realtime_conversation_item_user_message.py
    │       │   │   │   │   realtime_conversation_item_user_message_param.py
    │       │   │   │   │   realtime_error.py
    │       │   │   │   │   realtime_error_event.py
    │       │   │   │   │   realtime_function_tool.py
    │       │   │   │   │   realtime_function_tool_param.py
    │       │   │   │   │   realtime_mcphttp_error.py
    │       │   │   │   │   realtime_mcphttp_error_param.py
    │       │   │   │   │   realtime_mcp_approval_request.py
    │       │   │   │   │   realtime_mcp_approval_request_param.py
    │       │   │   │   │   realtime_mcp_approval_response.py
    │       │   │   │   │   realtime_mcp_approval_response_param.py
    │       │   │   │   │   realtime_mcp_list_tools.py
    │       │   │   │   │   realtime_mcp_list_tools_param.py
    │       │   │   │   │   realtime_mcp_protocol_error.py
    │       │   │   │   │   realtime_mcp_protocol_error_param.py
    │       │   │   │   │   realtime_mcp_tool_call.py
    │       │   │   │   │   realtime_mcp_tool_call_param.py
    │       │   │   │   │   realtime_mcp_tool_execution_error.py
    │       │   │   │   │   realtime_mcp_tool_execution_error_param.py
    │       │   │   │   │   realtime_reasoning.py
    │       │   │   │   │   realtime_reasoning_effort.py
    │       │   │   │   │   realtime_reasoning_param.py
    │       │   │   │   │   realtime_response.py
    │       │   │   │   │   realtime_response_create_audio_output.py
    │       │   │   │   │   realtime_response_create_audio_output_param.py
    │       │   │   │   │   realtime_response_create_mcp_tool.py
    │       │   │   │   │   realtime_response_create_mcp_tool_param.py
    │       │   │   │   │   realtime_response_create_params.py
    │       │   │   │   │   realtime_response_create_params_param.py
    │       │   │   │   │   realtime_response_status.py
    │       │   │   │   │   realtime_response_usage.py
    │       │   │   │   │   realtime_response_usage_input_token_details.py
    │       │   │   │   │   realtime_response_usage_output_token_details.py
    │       │   │   │   │   realtime_server_event.py
    │       │   │   │   │   realtime_session_create_request.py
    │       │   │   │   │   realtime_session_create_request_param.py
    │       │   │   │   │   realtime_session_create_response.py
    │       │   │   │   │   realtime_tools_config.py
    │       │   │   │   │   realtime_tools_config_param.py
    │       │   │   │   │   realtime_tools_config_union.py
    │       │   │   │   │   realtime_tools_config_union_param.py
    │       │   │   │   │   realtime_tool_choice_config.py
    │       │   │   │   │   realtime_tool_choice_config_param.py
    │       │   │   │   │   realtime_tracing_config.py
    │       │   │   │   │   realtime_tracing_config_param.py
    │       │   │   │   │   realtime_transcription_session_audio.py
    │       │   │   │   │   realtime_transcription_session_audio_input.py
    │       │   │   │   │   realtime_transcription_session_audio_input_param.py
    │       │   │   │   │   realtime_transcription_session_audio_input_turn_detection.py
    │       │   │   │   │   realtime_transcription_session_audio_input_turn_detection_param.py
    │       │   │   │   │   realtime_transcription_session_audio_param.py
    │       │   │   │   │   realtime_transcription_session_create_request.py
    │       │   │   │   │   realtime_transcription_session_create_request_param.py
    │       │   │   │   │   realtime_transcription_session_create_response.py
    │       │   │   │   │   realtime_transcription_session_turn_detection.py
    │       │   │   │   │   realtime_truncation.py
    │       │   │   │   │   realtime_truncation_param.py
    │       │   │   │   │   realtime_truncation_retention_ratio.py
    │       │   │   │   │   realtime_truncation_retention_ratio_param.py
    │       │   │   │   │   response_audio_delta_event.py
    │       │   │   │   │   response_audio_done_event.py
    │       │   │   │   │   response_audio_transcript_delta_event.py
    │       │   │   │   │   response_audio_transcript_done_event.py
    │       │   │   │   │   response_cancel_event.py
    │       │   │   │   │   response_cancel_event_param.py
    │       │   │   │   │   response_content_part_added_event.py
    │       │   │   │   │   response_content_part_done_event.py
    │       │   │   │   │   response_created_event.py
    │       │   │   │   │   response_create_event.py
    │       │   │   │   │   response_create_event_param.py
    │       │   │   │   │   response_done_event.py
    │       │   │   │   │   response_function_call_arguments_delta_event.py
    │       │   │   │   │   response_function_call_arguments_done_event.py
    │       │   │   │   │   response_mcp_call_arguments_delta.py
    │       │   │   │   │   response_mcp_call_arguments_done.py
    │       │   │   │   │   response_mcp_call_completed.py
    │       │   │   │   │   response_mcp_call_failed.py
    │       │   │   │   │   response_mcp_call_in_progress.py
    │       │   │   │   │   response_output_item_added_event.py
    │       │   │   │   │   response_output_item_done_event.py
    │       │   │   │   │   response_text_delta_event.py
    │       │   │   │   │   response_text_done_event.py
    │       │   │   │   │   session_created_event.py
    │       │   │   │   │   session_updated_event.py
    │       │   │   │   │   session_update_event.py
    │       │   │   │   │   session_update_event_param.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           audio_transcription.cpython-314.pyc
    │       │   │   │           audio_transcription_param.cpython-314.pyc
    │       │   │   │           call_accept_params.cpython-314.pyc
    │       │   │   │           call_create_params.cpython-314.pyc
    │       │   │   │           call_refer_params.cpython-314.pyc
    │       │   │   │           call_reject_params.cpython-314.pyc
    │       │   │   │           client_secret_create_params.cpython-314.pyc
    │       │   │   │           client_secret_create_response.cpython-314.pyc
    │       │   │   │           conversation_created_event.cpython-314.pyc
    │       │   │   │           conversation_item.cpython-314.pyc
    │       │   │   │           conversation_item_added.cpython-314.pyc
    │       │   │   │           conversation_item_created_event.cpython-314.pyc
    │       │   │   │           conversation_item_create_event.cpython-314.pyc
    │       │   │   │           conversation_item_create_event_param.cpython-314.pyc
    │       │   │   │           conversation_item_deleted_event.cpython-314.pyc
    │       │   │   │           conversation_item_delete_event.cpython-314.pyc
    │       │   │   │           conversation_item_delete_event_param.cpython-314.pyc
    │       │   │   │           conversation_item_done.cpython-314.pyc
    │       │   │   │           conversation_item_input_audio_transcription_completed_event.cpython-314.pyc
    │       │   │   │           conversation_item_input_audio_transcription_delta_event.cpython-314.pyc
    │       │   │   │           conversation_item_input_audio_transcription_failed_event.cpython-314.pyc
    │       │   │   │           conversation_item_input_audio_transcription_segment.cpython-314.pyc
    │       │   │   │           conversation_item_param.cpython-314.pyc
    │       │   │   │           conversation_item_retrieve_event.cpython-314.pyc
    │       │   │   │           conversation_item_retrieve_event_param.cpython-314.pyc
    │       │   │   │           conversation_item_truncated_event.cpython-314.pyc
    │       │   │   │           conversation_item_truncate_event.cpython-314.pyc
    │       │   │   │           conversation_item_truncate_event_param.cpython-314.pyc
    │       │   │   │           input_audio_buffer_append_event.cpython-314.pyc
    │       │   │   │           input_audio_buffer_append_event_param.cpython-314.pyc
    │       │   │   │           input_audio_buffer_cleared_event.cpython-314.pyc
    │       │   │   │           input_audio_buffer_clear_event.cpython-314.pyc
    │       │   │   │           input_audio_buffer_clear_event_param.cpython-314.pyc
    │       │   │   │           input_audio_buffer_committed_event.cpython-314.pyc
    │       │   │   │           input_audio_buffer_commit_event.cpython-314.pyc
    │       │   │   │           input_audio_buffer_commit_event_param.cpython-314.pyc
    │       │   │   │           input_audio_buffer_dtmf_event_received_event.cpython-314.pyc
    │       │   │   │           input_audio_buffer_speech_started_event.cpython-314.pyc
    │       │   │   │           input_audio_buffer_speech_stopped_event.cpython-314.pyc
    │       │   │   │           input_audio_buffer_timeout_triggered.cpython-314.pyc
    │       │   │   │           log_prob_properties.cpython-314.pyc
    │       │   │   │           mcp_list_tools_completed.cpython-314.pyc
    │       │   │   │           mcp_list_tools_failed.cpython-314.pyc
    │       │   │   │           mcp_list_tools_in_progress.cpython-314.pyc
    │       │   │   │           noise_reduction_type.cpython-314.pyc
    │       │   │   │           output_audio_buffer_clear_event.cpython-314.pyc
    │       │   │   │           output_audio_buffer_clear_event_param.cpython-314.pyc
    │       │   │   │           rate_limits_updated_event.cpython-314.pyc
    │       │   │   │           realtime_audio_config.cpython-314.pyc
    │       │   │   │           realtime_audio_config_input.cpython-314.pyc
    │       │   │   │           realtime_audio_config_input_param.cpython-314.pyc
    │       │   │   │           realtime_audio_config_output.cpython-314.pyc
    │       │   │   │           realtime_audio_config_output_param.cpython-314.pyc
    │       │   │   │           realtime_audio_config_param.cpython-314.pyc
    │       │   │   │           realtime_audio_formats.cpython-314.pyc
    │       │   │   │           realtime_audio_formats_param.cpython-314.pyc
    │       │   │   │           realtime_audio_input_turn_detection.cpython-314.pyc
    │       │   │   │           realtime_audio_input_turn_detection_param.cpython-314.pyc
    │       │   │   │           realtime_client_event.cpython-314.pyc
    │       │   │   │           realtime_client_event_param.cpython-314.pyc
    │       │   │   │           realtime_connect_params.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_assistant_message.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_assistant_message_param.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_function_call.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_function_call_output.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_function_call_output_param.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_function_call_param.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_system_message.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_system_message_param.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_user_message.cpython-314.pyc
    │       │   │   │           realtime_conversation_item_user_message_param.cpython-314.pyc
    │       │   │   │           realtime_error.cpython-314.pyc
    │       │   │   │           realtime_error_event.cpython-314.pyc
    │       │   │   │           realtime_function_tool.cpython-314.pyc
    │       │   │   │           realtime_function_tool_param.cpython-314.pyc
    │       │   │   │           realtime_mcphttp_error.cpython-314.pyc
    │       │   │   │           realtime_mcphttp_error_param.cpython-314.pyc
    │       │   │   │           realtime_mcp_approval_request.cpython-314.pyc
    │       │   │   │           realtime_mcp_approval_request_param.cpython-314.pyc
    │       │   │   │           realtime_mcp_approval_response.cpython-314.pyc
    │       │   │   │           realtime_mcp_approval_response_param.cpython-314.pyc
    │       │   │   │           realtime_mcp_list_tools.cpython-314.pyc
    │       │   │   │           realtime_mcp_list_tools_param.cpython-314.pyc
    │       │   │   │           realtime_mcp_protocol_error.cpython-314.pyc
    │       │   │   │           realtime_mcp_protocol_error_param.cpython-314.pyc
    │       │   │   │           realtime_mcp_tool_call.cpython-314.pyc
    │       │   │   │           realtime_mcp_tool_call_param.cpython-314.pyc
    │       │   │   │           realtime_mcp_tool_execution_error.cpython-314.pyc
    │       │   │   │           realtime_mcp_tool_execution_error_param.cpython-314.pyc
    │       │   │   │           realtime_reasoning.cpython-314.pyc
    │       │   │   │           realtime_reasoning_effort.cpython-314.pyc
    │       │   │   │           realtime_reasoning_param.cpython-314.pyc
    │       │   │   │           realtime_response.cpython-314.pyc
    │       │   │   │           realtime_response_create_audio_output.cpython-314.pyc
    │       │   │   │           realtime_response_create_audio_output_param.cpython-314.pyc
    │       │   │   │           realtime_response_create_mcp_tool.cpython-314.pyc
    │       │   │   │           realtime_response_create_mcp_tool_param.cpython-314.pyc
    │       │   │   │           realtime_response_create_params.cpython-314.pyc
    │       │   │   │           realtime_response_create_params_param.cpython-314.pyc
    │       │   │   │           realtime_response_status.cpython-314.pyc
    │       │   │   │           realtime_response_usage.cpython-314.pyc
    │       │   │   │           realtime_response_usage_input_token_details.cpython-314.pyc
    │       │   │   │           realtime_response_usage_output_token_details.cpython-314.pyc
    │       │   │   │           realtime_server_event.cpython-314.pyc
    │       │   │   │           realtime_session_create_request.cpython-314.pyc
    │       │   │   │           realtime_session_create_request_param.cpython-314.pyc
    │       │   │   │           realtime_session_create_response.cpython-314.pyc
    │       │   │   │           realtime_tools_config.cpython-314.pyc
    │       │   │   │           realtime_tools_config_param.cpython-314.pyc
    │       │   │   │           realtime_tools_config_union.cpython-314.pyc
    │       │   │   │           realtime_tools_config_union_param.cpython-314.pyc
    │       │   │   │           realtime_tool_choice_config.cpython-314.pyc
    │       │   │   │           realtime_tool_choice_config_param.cpython-314.pyc
    │       │   │   │           realtime_tracing_config.cpython-314.pyc
    │       │   │   │           realtime_tracing_config_param.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_audio.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_audio_input.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_audio_input_param.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_audio_input_turn_detection.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_audio_input_turn_detection_param.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_audio_param.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_create_request.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_create_request_param.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_create_response.cpython-314.pyc
    │       │   │   │           realtime_transcription_session_turn_detection.cpython-314.pyc
    │       │   │   │           realtime_truncation.cpython-314.pyc
    │       │   │   │           realtime_truncation_param.cpython-314.pyc
    │       │   │   │           realtime_truncation_retention_ratio.cpython-314.pyc
    │       │   │   │           realtime_truncation_retention_ratio_param.cpython-314.pyc
    │       │   │   │           response_audio_delta_event.cpython-314.pyc
    │       │   │   │           response_audio_done_event.cpython-314.pyc
    │       │   │   │           response_audio_transcript_delta_event.cpython-314.pyc
    │       │   │   │           response_audio_transcript_done_event.cpython-314.pyc
    │       │   │   │           response_cancel_event.cpython-314.pyc
    │       │   │   │           response_cancel_event_param.cpython-314.pyc
    │       │   │   │           response_content_part_added_event.cpython-314.pyc
    │       │   │   │           response_content_part_done_event.cpython-314.pyc
    │       │   │   │           response_created_event.cpython-314.pyc
    │       │   │   │           response_create_event.cpython-314.pyc
    │       │   │   │           response_create_event_param.cpython-314.pyc
    │       │   │   │           response_done_event.cpython-314.pyc
    │       │   │   │           response_function_call_arguments_delta_event.cpython-314.pyc
    │       │   │   │           response_function_call_arguments_done_event.cpython-314.pyc
    │       │   │   │           response_mcp_call_arguments_delta.cpython-314.pyc
    │       │   │   │           response_mcp_call_arguments_done.cpython-314.pyc
    │       │   │   │           response_mcp_call_completed.cpython-314.pyc
    │       │   │   │           response_mcp_call_failed.cpython-314.pyc
    │       │   │   │           response_mcp_call_in_progress.cpython-314.pyc
    │       │   │   │           response_output_item_added_event.cpython-314.pyc
    │       │   │   │           response_output_item_done_event.cpython-314.pyc
    │       │   │   │           response_text_delta_event.cpython-314.pyc
    │       │   │   │           response_text_done_event.cpython-314.pyc
    │       │   │   │           session_created_event.cpython-314.pyc
    │       │   │   │           session_updated_event.cpython-314.pyc
    │       │   │   │           session_update_event.cpython-314.pyc
    │       │   │   │           session_update_event_param.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───responses
    │       │   │   │   │   apply_patch_tool.py
    │       │   │   │   │   apply_patch_tool_param.py
    │       │   │   │   │   compacted_response.py
    │       │   │   │   │   computer_action.py
    │       │   │   │   │   computer_action_list.py
    │       │   │   │   │   computer_action_list_param.py
    │       │   │   │   │   computer_action_param.py
    │       │   │   │   │   computer_tool.py
    │       │   │   │   │   computer_tool_param.py
    │       │   │   │   │   computer_use_preview_tool.py
    │       │   │   │   │   computer_use_preview_tool_param.py
    │       │   │   │   │   container_auto.py
    │       │   │   │   │   container_auto_param.py
    │       │   │   │   │   container_network_policy_allowlist.py
    │       │   │   │   │   container_network_policy_allowlist_param.py
    │       │   │   │   │   container_network_policy_disabled.py
    │       │   │   │   │   container_network_policy_disabled_param.py
    │       │   │   │   │   container_network_policy_domain_secret.py
    │       │   │   │   │   container_network_policy_domain_secret_param.py
    │       │   │   │   │   container_reference.py
    │       │   │   │   │   container_reference_param.py
    │       │   │   │   │   custom_tool.py
    │       │   │   │   │   custom_tool_param.py
    │       │   │   │   │   easy_input_message.py
    │       │   │   │   │   easy_input_message_param.py
    │       │   │   │   │   file_search_tool.py
    │       │   │   │   │   file_search_tool_param.py
    │       │   │   │   │   function_shell_tool.py
    │       │   │   │   │   function_shell_tool_param.py
    │       │   │   │   │   function_tool.py
    │       │   │   │   │   function_tool_param.py
    │       │   │   │   │   inline_skill.py
    │       │   │   │   │   inline_skill_param.py
    │       │   │   │   │   inline_skill_source.py
    │       │   │   │   │   inline_skill_source_param.py
    │       │   │   │   │   input_item_list_params.py
    │       │   │   │   │   input_token_count_params.py
    │       │   │   │   │   input_token_count_response.py
    │       │   │   │   │   local_environment.py
    │       │   │   │   │   local_environment_param.py
    │       │   │   │   │   local_skill.py
    │       │   │   │   │   local_skill_param.py
    │       │   │   │   │   namespace_tool.py
    │       │   │   │   │   namespace_tool_param.py
    │       │   │   │   │   parsed_response.py
    │       │   │   │   │   response.py
    │       │   │   │   │   responses_client_event.py
    │       │   │   │   │   responses_client_event_param.py
    │       │   │   │   │   responses_server_event.py
    │       │   │   │   │   response_apply_patch_tool_call.py
    │       │   │   │   │   response_apply_patch_tool_call_output.py
    │       │   │   │   │   response_audio_delta_event.py
    │       │   │   │   │   response_audio_done_event.py
    │       │   │   │   │   response_audio_transcript_delta_event.py
    │       │   │   │   │   response_audio_transcript_done_event.py
    │       │   │   │   │   response_code_interpreter_call_code_delta_event.py
    │       │   │   │   │   response_code_interpreter_call_code_done_event.py
    │       │   │   │   │   response_code_interpreter_call_completed_event.py
    │       │   │   │   │   response_code_interpreter_call_interpreting_event.py
    │       │   │   │   │   response_code_interpreter_call_in_progress_event.py
    │       │   │   │   │   response_code_interpreter_tool_call.py
    │       │   │   │   │   response_code_interpreter_tool_call_param.py
    │       │   │   │   │   response_compaction_item.py
    │       │   │   │   │   response_compaction_item_param.py
    │       │   │   │   │   response_compaction_item_param_param.py
    │       │   │   │   │   response_compact_params.py
    │       │   │   │   │   response_completed_event.py
    │       │   │   │   │   response_computer_tool_call.py
    │       │   │   │   │   response_computer_tool_call_output_item.py
    │       │   │   │   │   response_computer_tool_call_output_screenshot.py
    │       │   │   │   │   response_computer_tool_call_output_screenshot_param.py
    │       │   │   │   │   response_computer_tool_call_param.py
    │       │   │   │   │   response_container_reference.py
    │       │   │   │   │   response_content_part_added_event.py
    │       │   │   │   │   response_content_part_done_event.py
    │       │   │   │   │   response_conversation_param.py
    │       │   │   │   │   response_conversation_param_param.py
    │       │   │   │   │   response_created_event.py
    │       │   │   │   │   response_create_params.py
    │       │   │   │   │   response_custom_tool_call.py
    │       │   │   │   │   response_custom_tool_call_input_delta_event.py
    │       │   │   │   │   response_custom_tool_call_input_done_event.py
    │       │   │   │   │   response_custom_tool_call_item.py
    │       │   │   │   │   response_custom_tool_call_output.py
    │       │   │   │   │   response_custom_tool_call_output_item.py
    │       │   │   │   │   response_custom_tool_call_output_param.py
    │       │   │   │   │   response_custom_tool_call_param.py
    │       │   │   │   │   response_error.py
    │       │   │   │   │   response_error_event.py
    │       │   │   │   │   response_failed_event.py
    │       │   │   │   │   response_file_search_call_completed_event.py
    │       │   │   │   │   response_file_search_call_in_progress_event.py
    │       │   │   │   │   response_file_search_call_searching_event.py
    │       │   │   │   │   response_file_search_tool_call.py
    │       │   │   │   │   response_file_search_tool_call_param.py
    │       │   │   │   │   response_format_text_config.py
    │       │   │   │   │   response_format_text_config_param.py
    │       │   │   │   │   response_format_text_json_schema_config.py
    │       │   │   │   │   response_format_text_json_schema_config_param.py
    │       │   │   │   │   response_function_call_arguments_delta_event.py
    │       │   │   │   │   response_function_call_arguments_done_event.py
    │       │   │   │   │   response_function_call_output_item.py
    │       │   │   │   │   response_function_call_output_item_list.py
    │       │   │   │   │   response_function_call_output_item_list_param.py
    │       │   │   │   │   response_function_call_output_item_param.py
    │       │   │   │   │   response_function_shell_call_output_content.py
    │       │   │   │   │   response_function_shell_call_output_content_param.py
    │       │   │   │   │   response_function_shell_tool_call.py
    │       │   │   │   │   response_function_shell_tool_call_output.py
    │       │   │   │   │   response_function_tool_call.py
    │       │   │   │   │   response_function_tool_call_item.py
    │       │   │   │   │   response_function_tool_call_output_item.py
    │       │   │   │   │   response_function_tool_call_param.py
    │       │   │   │   │   response_function_web_search.py
    │       │   │   │   │   response_function_web_search_param.py
    │       │   │   │   │   response_image_gen_call_completed_event.py
    │       │   │   │   │   response_image_gen_call_generating_event.py
    │       │   │   │   │   response_image_gen_call_in_progress_event.py
    │       │   │   │   │   response_image_gen_call_partial_image_event.py
    │       │   │   │   │   response_includable.py
    │       │   │   │   │   response_incomplete_event.py
    │       │   │   │   │   response_input.py
    │       │   │   │   │   response_input_audio.py
    │       │   │   │   │   response_input_audio_param.py
    │       │   │   │   │   response_input_content.py
    │       │   │   │   │   response_input_content_param.py
    │       │   │   │   │   response_input_file.py
    │       │   │   │   │   response_input_file_content.py
    │       │   │   │   │   response_input_file_content_param.py
    │       │   │   │   │   response_input_file_param.py
    │       │   │   │   │   response_input_image.py
    │       │   │   │   │   response_input_image_content.py
    │       │   │   │   │   response_input_image_content_param.py
    │       │   │   │   │   response_input_image_param.py
    │       │   │   │   │   response_input_item.py
    │       │   │   │   │   response_input_item_param.py
    │       │   │   │   │   response_input_message_content_list.py
    │       │   │   │   │   response_input_message_content_list_param.py
    │       │   │   │   │   response_input_message_item.py
    │       │   │   │   │   response_input_param.py
    │       │   │   │   │   response_input_text.py
    │       │   │   │   │   response_input_text_content.py
    │       │   │   │   │   response_input_text_content_param.py
    │       │   │   │   │   response_input_text_param.py
    │       │   │   │   │   response_in_progress_event.py
    │       │   │   │   │   response_item.py
    │       │   │   │   │   response_item_list.py
    │       │   │   │   │   response_local_environment.py
    │       │   │   │   │   response_mcp_call_arguments_delta_event.py
    │       │   │   │   │   response_mcp_call_arguments_done_event.py
    │       │   │   │   │   response_mcp_call_completed_event.py
    │       │   │   │   │   response_mcp_call_failed_event.py
    │       │   │   │   │   response_mcp_call_in_progress_event.py
    │       │   │   │   │   response_mcp_list_tools_completed_event.py
    │       │   │   │   │   response_mcp_list_tools_failed_event.py
    │       │   │   │   │   response_mcp_list_tools_in_progress_event.py
    │       │   │   │   │   response_output_item.py
    │       │   │   │   │   response_output_item_added_event.py
    │       │   │   │   │   response_output_item_done_event.py
    │       │   │   │   │   response_output_message.py
    │       │   │   │   │   response_output_message_param.py
    │       │   │   │   │   response_output_refusal.py
    │       │   │   │   │   response_output_refusal_param.py
    │       │   │   │   │   response_output_text.py
    │       │   │   │   │   response_output_text_annotation_added_event.py
    │       │   │   │   │   response_output_text_param.py
    │       │   │   │   │   response_prompt.py
    │       │   │   │   │   response_prompt_param.py
    │       │   │   │   │   response_queued_event.py
    │       │   │   │   │   response_reasoning_item.py
    │       │   │   │   │   response_reasoning_item_param.py
    │       │   │   │   │   response_reasoning_summary_part_added_event.py
    │       │   │   │   │   response_reasoning_summary_part_done_event.py
    │       │   │   │   │   response_reasoning_summary_text_delta_event.py
    │       │   │   │   │   response_reasoning_summary_text_done_event.py
    │       │   │   │   │   response_reasoning_text_delta_event.py
    │       │   │   │   │   response_reasoning_text_done_event.py
    │       │   │   │   │   response_refusal_delta_event.py
    │       │   │   │   │   response_refusal_done_event.py
    │       │   │   │   │   response_retrieve_params.py
    │       │   │   │   │   response_status.py
    │       │   │   │   │   response_stream_event.py
    │       │   │   │   │   response_text_config.py
    │       │   │   │   │   response_text_config_param.py
    │       │   │   │   │   response_text_delta_event.py
    │       │   │   │   │   response_text_done_event.py
    │       │   │   │   │   response_tool_search_call.py
    │       │   │   │   │   response_tool_search_output_item.py
    │       │   │   │   │   response_tool_search_output_item_param.py
    │       │   │   │   │   response_tool_search_output_item_param_param.py
    │       │   │   │   │   response_usage.py
    │       │   │   │   │   response_web_search_call_completed_event.py
    │       │   │   │   │   response_web_search_call_in_progress_event.py
    │       │   │   │   │   response_web_search_call_searching_event.py
    │       │   │   │   │   skill_reference.py
    │       │   │   │   │   skill_reference_param.py
    │       │   │   │   │   tool.py
    │       │   │   │   │   tool_choice_allowed.py
    │       │   │   │   │   tool_choice_allowed_param.py
    │       │   │   │   │   tool_choice_apply_patch.py
    │       │   │   │   │   tool_choice_apply_patch_param.py
    │       │   │   │   │   tool_choice_custom.py
    │       │   │   │   │   tool_choice_custom_param.py
    │       │   │   │   │   tool_choice_function.py
    │       │   │   │   │   tool_choice_function_param.py
    │       │   │   │   │   tool_choice_mcp.py
    │       │   │   │   │   tool_choice_mcp_param.py
    │       │   │   │   │   tool_choice_options.py
    │       │   │   │   │   tool_choice_shell.py
    │       │   │   │   │   tool_choice_shell_param.py
    │       │   │   │   │   tool_choice_types.py
    │       │   │   │   │   tool_choice_types_param.py
    │       │   │   │   │   tool_param.py
    │       │   │   │   │   tool_search_tool.py
    │       │   │   │   │   tool_search_tool_param.py
    │       │   │   │   │   web_search_preview_tool.py
    │       │   │   │   │   web_search_preview_tool_param.py
    │       │   │   │   │   web_search_tool.py
    │       │   │   │   │   web_search_tool_param.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           apply_patch_tool.cpython-314.pyc
    │       │   │   │           apply_patch_tool_param.cpython-314.pyc
    │       │   │   │           compacted_response.cpython-314.pyc
    │       │   │   │           computer_action.cpython-314.pyc
    │       │   │   │           computer_action_list.cpython-314.pyc
    │       │   │   │           computer_action_list_param.cpython-314.pyc
    │       │   │   │           computer_action_param.cpython-314.pyc
    │       │   │   │           computer_tool.cpython-314.pyc
    │       │   │   │           computer_tool_param.cpython-314.pyc
    │       │   │   │           computer_use_preview_tool.cpython-314.pyc
    │       │   │   │           computer_use_preview_tool_param.cpython-314.pyc
    │       │   │   │           container_auto.cpython-314.pyc
    │       │   │   │           container_auto_param.cpython-314.pyc
    │       │   │   │           container_network_policy_allowlist.cpython-314.pyc
    │       │   │   │           container_network_policy_allowlist_param.cpython-314.pyc
    │       │   │   │           container_network_policy_disabled.cpython-314.pyc
    │       │   │   │           container_network_policy_disabled_param.cpython-314.pyc
    │       │   │   │           container_network_policy_domain_secret.cpython-314.pyc
    │       │   │   │           container_network_policy_domain_secret_param.cpython-314.pyc
    │       │   │   │           container_reference.cpython-314.pyc
    │       │   │   │           container_reference_param.cpython-314.pyc
    │       │   │   │           custom_tool.cpython-314.pyc
    │       │   │   │           custom_tool_param.cpython-314.pyc
    │       │   │   │           easy_input_message.cpython-314.pyc
    │       │   │   │           easy_input_message_param.cpython-314.pyc
    │       │   │   │           file_search_tool.cpython-314.pyc
    │       │   │   │           file_search_tool_param.cpython-314.pyc
    │       │   │   │           function_shell_tool.cpython-314.pyc
    │       │   │   │           function_shell_tool_param.cpython-314.pyc
    │       │   │   │           function_tool.cpython-314.pyc
    │       │   │   │           function_tool_param.cpython-314.pyc
    │       │   │   │           inline_skill.cpython-314.pyc
    │       │   │   │           inline_skill_param.cpython-314.pyc
    │       │   │   │           inline_skill_source.cpython-314.pyc
    │       │   │   │           inline_skill_source_param.cpython-314.pyc
    │       │   │   │           input_item_list_params.cpython-314.pyc
    │       │   │   │           input_token_count_params.cpython-314.pyc
    │       │   │   │           input_token_count_response.cpython-314.pyc
    │       │   │   │           local_environment.cpython-314.pyc
    │       │   │   │           local_environment_param.cpython-314.pyc
    │       │   │   │           local_skill.cpython-314.pyc
    │       │   │   │           local_skill_param.cpython-314.pyc
    │       │   │   │           namespace_tool.cpython-314.pyc
    │       │   │   │           namespace_tool_param.cpython-314.pyc
    │       │   │   │           parsed_response.cpython-314.pyc
    │       │   │   │           response.cpython-314.pyc
    │       │   │   │           responses_client_event.cpython-314.pyc
    │       │   │   │           responses_client_event_param.cpython-314.pyc
    │       │   │   │           responses_server_event.cpython-314.pyc
    │       │   │   │           response_apply_patch_tool_call.cpython-314.pyc
    │       │   │   │           response_apply_patch_tool_call_output.cpython-314.pyc
    │       │   │   │           response_audio_delta_event.cpython-314.pyc
    │       │   │   │           response_audio_done_event.cpython-314.pyc
    │       │   │   │           response_audio_transcript_delta_event.cpython-314.pyc
    │       │   │   │           response_audio_transcript_done_event.cpython-314.pyc
    │       │   │   │           response_code_interpreter_call_code_delta_event.cpython-314.pyc
    │       │   │   │           response_code_interpreter_call_code_done_event.cpython-314.pyc
    │       │   │   │           response_code_interpreter_call_completed_event.cpython-314.pyc
    │       │   │   │           response_code_interpreter_call_interpreting_event.cpython-314.pyc
    │       │   │   │           response_code_interpreter_call_in_progress_event.cpython-314.pyc
    │       │   │   │           response_code_interpreter_tool_call.cpython-314.pyc
    │       │   │   │           response_code_interpreter_tool_call_param.cpython-314.pyc
    │       │   │   │           response_compaction_item.cpython-314.pyc
    │       │   │   │           response_compaction_item_param.cpython-314.pyc
    │       │   │   │           response_compaction_item_param_param.cpython-314.pyc
    │       │   │   │           response_compact_params.cpython-314.pyc
    │       │   │   │           response_completed_event.cpython-314.pyc
    │       │   │   │           response_computer_tool_call.cpython-314.pyc
    │       │   │   │           response_computer_tool_call_output_item.cpython-314.pyc
    │       │   │   │           response_computer_tool_call_output_screenshot.cpython-314.pyc
    │       │   │   │           response_computer_tool_call_output_screenshot_param.cpython-314.pyc
    │       │   │   │           response_computer_tool_call_param.cpython-314.pyc
    │       │   │   │           response_container_reference.cpython-314.pyc
    │       │   │   │           response_content_part_added_event.cpython-314.pyc
    │       │   │   │           response_content_part_done_event.cpython-314.pyc
    │       │   │   │           response_conversation_param.cpython-314.pyc
    │       │   │   │           response_conversation_param_param.cpython-314.pyc
    │       │   │   │           response_created_event.cpython-314.pyc
    │       │   │   │           response_create_params.cpython-314.pyc
    │       │   │   │           response_custom_tool_call.cpython-314.pyc
    │       │   │   │           response_custom_tool_call_input_delta_event.cpython-314.pyc
    │       │   │   │           response_custom_tool_call_input_done_event.cpython-314.pyc
    │       │   │   │           response_custom_tool_call_item.cpython-314.pyc
    │       │   │   │           response_custom_tool_call_output.cpython-314.pyc
    │       │   │   │           response_custom_tool_call_output_item.cpython-314.pyc
    │       │   │   │           response_custom_tool_call_output_param.cpython-314.pyc
    │       │   │   │           response_custom_tool_call_param.cpython-314.pyc
    │       │   │   │           response_error.cpython-314.pyc
    │       │   │   │           response_error_event.cpython-314.pyc
    │       │   │   │           response_failed_event.cpython-314.pyc
    │       │   │   │           response_file_search_call_completed_event.cpython-314.pyc
    │       │   │   │           response_file_search_call_in_progress_event.cpython-314.pyc
    │       │   │   │           response_file_search_call_searching_event.cpython-314.pyc
    │       │   │   │           response_file_search_tool_call.cpython-314.pyc
    │       │   │   │           response_file_search_tool_call_param.cpython-314.pyc
    │       │   │   │           response_format_text_config.cpython-314.pyc
    │       │   │   │           response_format_text_config_param.cpython-314.pyc
    │       │   │   │           response_format_text_json_schema_config.cpython-314.pyc
    │       │   │   │           response_format_text_json_schema_config_param.cpython-314.pyc
    │       │   │   │           response_function_call_arguments_delta_event.cpython-314.pyc
    │       │   │   │           response_function_call_arguments_done_event.cpython-314.pyc
    │       │   │   │           response_function_call_output_item.cpython-314.pyc
    │       │   │   │           response_function_call_output_item_list.cpython-314.pyc
    │       │   │   │           response_function_call_output_item_list_param.cpython-314.pyc
    │       │   │   │           response_function_call_output_item_param.cpython-314.pyc
    │       │   │   │           response_function_shell_call_output_content.cpython-314.pyc
    │       │   │   │           response_function_shell_call_output_content_param.cpython-314.pyc
    │       │   │   │           response_function_shell_tool_call.cpython-314.pyc
    │       │   │   │           response_function_shell_tool_call_output.cpython-314.pyc
    │       │   │   │           response_function_tool_call.cpython-314.pyc
    │       │   │   │           response_function_tool_call_item.cpython-314.pyc
    │       │   │   │           response_function_tool_call_output_item.cpython-314.pyc
    │       │   │   │           response_function_tool_call_param.cpython-314.pyc
    │       │   │   │           response_function_web_search.cpython-314.pyc
    │       │   │   │           response_function_web_search_param.cpython-314.pyc
    │       │   │   │           response_image_gen_call_completed_event.cpython-314.pyc
    │       │   │   │           response_image_gen_call_generating_event.cpython-314.pyc
    │       │   │   │           response_image_gen_call_in_progress_event.cpython-314.pyc
    │       │   │   │           response_image_gen_call_partial_image_event.cpython-314.pyc
    │       │   │   │           response_includable.cpython-314.pyc
    │       │   │   │           response_incomplete_event.cpython-314.pyc
    │       │   │   │           response_input.cpython-314.pyc
    │       │   │   │           response_input_audio.cpython-314.pyc
    │       │   │   │           response_input_audio_param.cpython-314.pyc
    │       │   │   │           response_input_content.cpython-314.pyc
    │       │   │   │           response_input_content_param.cpython-314.pyc
    │       │   │   │           response_input_file.cpython-314.pyc
    │       │   │   │           response_input_file_content.cpython-314.pyc
    │       │   │   │           response_input_file_content_param.cpython-314.pyc
    │       │   │   │           response_input_file_param.cpython-314.pyc
    │       │   │   │           response_input_image.cpython-314.pyc
    │       │   │   │           response_input_image_content.cpython-314.pyc
    │       │   │   │           response_input_image_content_param.cpython-314.pyc
    │       │   │   │           response_input_image_param.cpython-314.pyc
    │       │   │   │           response_input_item.cpython-314.pyc
    │       │   │   │           response_input_item_param.cpython-314.pyc
    │       │   │   │           response_input_message_content_list.cpython-314.pyc
    │       │   │   │           response_input_message_content_list_param.cpython-314.pyc
    │       │   │   │           response_input_message_item.cpython-314.pyc
    │       │   │   │           response_input_param.cpython-314.pyc
    │       │   │   │           response_input_text.cpython-314.pyc
    │       │   │   │           response_input_text_content.cpython-314.pyc
    │       │   │   │           response_input_text_content_param.cpython-314.pyc
    │       │   │   │           response_input_text_param.cpython-314.pyc
    │       │   │   │           response_in_progress_event.cpython-314.pyc
    │       │   │   │           response_item.cpython-314.pyc
    │       │   │   │           response_item_list.cpython-314.pyc
    │       │   │   │           response_local_environment.cpython-314.pyc
    │       │   │   │           response_mcp_call_arguments_delta_event.cpython-314.pyc
    │       │   │   │           response_mcp_call_arguments_done_event.cpython-314.pyc
    │       │   │   │           response_mcp_call_completed_event.cpython-314.pyc
    │       │   │   │           response_mcp_call_failed_event.cpython-314.pyc
    │       │   │   │           response_mcp_call_in_progress_event.cpython-314.pyc
    │       │   │   │           response_mcp_list_tools_completed_event.cpython-314.pyc
    │       │   │   │           response_mcp_list_tools_failed_event.cpython-314.pyc
    │       │   │   │           response_mcp_list_tools_in_progress_event.cpython-314.pyc
    │       │   │   │           response_output_item.cpython-314.pyc
    │       │   │   │           response_output_item_added_event.cpython-314.pyc
    │       │   │   │           response_output_item_done_event.cpython-314.pyc
    │       │   │   │           response_output_message.cpython-314.pyc
    │       │   │   │           response_output_message_param.cpython-314.pyc
    │       │   │   │           response_output_refusal.cpython-314.pyc
    │       │   │   │           response_output_refusal_param.cpython-314.pyc
    │       │   │   │           response_output_text.cpython-314.pyc
    │       │   │   │           response_output_text_annotation_added_event.cpython-314.pyc
    │       │   │   │           response_output_text_param.cpython-314.pyc
    │       │   │   │           response_prompt.cpython-314.pyc
    │       │   │   │           response_prompt_param.cpython-314.pyc
    │       │   │   │           response_queued_event.cpython-314.pyc
    │       │   │   │           response_reasoning_item.cpython-314.pyc
    │       │   │   │           response_reasoning_item_param.cpython-314.pyc
    │       │   │   │           response_reasoning_summary_part_added_event.cpython-314.pyc
    │       │   │   │           response_reasoning_summary_part_done_event.cpython-314.pyc
    │       │   │   │           response_reasoning_summary_text_delta_event.cpython-314.pyc
    │       │   │   │           response_reasoning_summary_text_done_event.cpython-314.pyc
    │       │   │   │           response_reasoning_text_delta_event.cpython-314.pyc
    │       │   │   │           response_reasoning_text_done_event.cpython-314.pyc
    │       │   │   │           response_refusal_delta_event.cpython-314.pyc
    │       │   │   │           response_refusal_done_event.cpython-314.pyc
    │       │   │   │           response_retrieve_params.cpython-314.pyc
    │       │   │   │           response_status.cpython-314.pyc
    │       │   │   │           response_stream_event.cpython-314.pyc
    │       │   │   │           response_text_config.cpython-314.pyc
    │       │   │   │           response_text_config_param.cpython-314.pyc
    │       │   │   │           response_text_delta_event.cpython-314.pyc
    │       │   │   │           response_text_done_event.cpython-314.pyc
    │       │   │   │           response_tool_search_call.cpython-314.pyc
    │       │   │   │           response_tool_search_output_item.cpython-314.pyc
    │       │   │   │           response_tool_search_output_item_param.cpython-314.pyc
    │       │   │   │           response_tool_search_output_item_param_param.cpython-314.pyc
    │       │   │   │           response_usage.cpython-314.pyc
    │       │   │   │           response_web_search_call_completed_event.cpython-314.pyc
    │       │   │   │           response_web_search_call_in_progress_event.cpython-314.pyc
    │       │   │   │           response_web_search_call_searching_event.cpython-314.pyc
    │       │   │   │           skill_reference.cpython-314.pyc
    │       │   │   │           skill_reference_param.cpython-314.pyc
    │       │   │   │           tool.cpython-314.pyc
    │       │   │   │           tool_choice_allowed.cpython-314.pyc
    │       │   │   │           tool_choice_allowed_param.cpython-314.pyc
    │       │   │   │           tool_choice_apply_patch.cpython-314.pyc
    │       │   │   │           tool_choice_apply_patch_param.cpython-314.pyc
    │       │   │   │           tool_choice_custom.cpython-314.pyc
    │       │   │   │           tool_choice_custom_param.cpython-314.pyc
    │       │   │   │           tool_choice_function.cpython-314.pyc
    │       │   │   │           tool_choice_function_param.cpython-314.pyc
    │       │   │   │           tool_choice_mcp.cpython-314.pyc
    │       │   │   │           tool_choice_mcp_param.cpython-314.pyc
    │       │   │   │           tool_choice_options.cpython-314.pyc
    │       │   │   │           tool_choice_shell.cpython-314.pyc
    │       │   │   │           tool_choice_shell_param.cpython-314.pyc
    │       │   │   │           tool_choice_types.cpython-314.pyc
    │       │   │   │           tool_choice_types_param.cpython-314.pyc
    │       │   │   │           tool_param.cpython-314.pyc
    │       │   │   │           tool_search_tool.cpython-314.pyc
    │       │   │   │           tool_search_tool_param.cpython-314.pyc
    │       │   │   │           web_search_preview_tool.cpython-314.pyc
    │       │   │   │           web_search_preview_tool_param.cpython-314.pyc
    │       │   │   │           web_search_tool.cpython-314.pyc
    │       │   │   │           web_search_tool_param.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───shared
    │       │   │   │   │   all_models.py
    │       │   │   │   │   chat_model.py
    │       │   │   │   │   comparison_filter.py
    │       │   │   │   │   compound_filter.py
    │       │   │   │   │   custom_tool_input_format.py
    │       │   │   │   │   error_object.py
    │       │   │   │   │   function_definition.py
    │       │   │   │   │   function_parameters.py
    │       │   │   │   │   metadata.py
    │       │   │   │   │   oauth_error_code.py
    │       │   │   │   │   reasoning.py
    │       │   │   │   │   reasoning_effort.py
    │       │   │   │   │   responses_model.py
    │       │   │   │   │   response_format_json_object.py
    │       │   │   │   │   response_format_json_schema.py
    │       │   │   │   │   response_format_text.py
    │       │   │   │   │   response_format_text_grammar.py
    │       │   │   │   │   response_format_text_python.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           all_models.cpython-314.pyc
    │       │   │   │           chat_model.cpython-314.pyc
    │       │   │   │           comparison_filter.cpython-314.pyc
    │       │   │   │           compound_filter.cpython-314.pyc
    │       │   │   │           custom_tool_input_format.cpython-314.pyc
    │       │   │   │           error_object.cpython-314.pyc
    │       │   │   │           function_definition.cpython-314.pyc
    │       │   │   │           function_parameters.cpython-314.pyc
    │       │   │   │           metadata.cpython-314.pyc
    │       │   │   │           oauth_error_code.cpython-314.pyc
    │       │   │   │           reasoning.cpython-314.pyc
    │       │   │   │           reasoning_effort.cpython-314.pyc
    │       │   │   │           responses_model.cpython-314.pyc
    │       │   │   │           response_format_json_object.cpython-314.pyc
    │       │   │   │           response_format_json_schema.cpython-314.pyc
    │       │   │   │           response_format_text.cpython-314.pyc
    │       │   │   │           response_format_text_grammar.cpython-314.pyc
    │       │   │   │           response_format_text_python.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───shared_params
    │       │   │   │   │   chat_model.py
    │       │   │   │   │   comparison_filter.py
    │       │   │   │   │   compound_filter.py
    │       │   │   │   │   custom_tool_input_format.py
    │       │   │   │   │   function_definition.py
    │       │   │   │   │   function_parameters.py
    │       │   │   │   │   metadata.py
    │       │   │   │   │   oauth_error_code.py
    │       │   │   │   │   reasoning.py
    │       │   │   │   │   reasoning_effort.py
    │       │   │   │   │   responses_model.py
    │       │   │   │   │   response_format_json_object.py
    │       │   │   │   │   response_format_json_schema.py
    │       │   │   │   │   response_format_text.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           chat_model.cpython-314.pyc
    │       │   │   │           comparison_filter.cpython-314.pyc
    │       │   │   │           compound_filter.cpython-314.pyc
    │       │   │   │           custom_tool_input_format.cpython-314.pyc
    │       │   │   │           function_definition.cpython-314.pyc
    │       │   │   │           function_parameters.cpython-314.pyc
    │       │   │   │           metadata.cpython-314.pyc
    │       │   │   │           oauth_error_code.cpython-314.pyc
    │       │   │   │           reasoning.cpython-314.pyc
    │       │   │   │           reasoning_effort.cpython-314.pyc
    │       │   │   │           responses_model.cpython-314.pyc
    │       │   │   │           response_format_json_object.cpython-314.pyc
    │       │   │   │           response_format_json_schema.cpython-314.pyc
    │       │   │   │           response_format_text.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───skills
    │       │   │   │   │   deleted_skill_version.py
    │       │   │   │   │   skill_version.py
    │       │   │   │   │   skill_version_list.py
    │       │   │   │   │   version_create_params.py
    │       │   │   │   │   version_list_params.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───versions
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           deleted_skill_version.cpython-314.pyc
    │       │   │   │           skill_version.cpython-314.pyc
    │       │   │   │           skill_version_list.cpython-314.pyc
    │       │   │   │           version_create_params.cpython-314.pyc
    │       │   │   │           version_list_params.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───uploads
    │       │   │   │   │   part_create_params.py
    │       │   │   │   │   upload_part.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           part_create_params.cpython-314.pyc
    │       │   │   │           upload_part.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───vector_stores
    │       │   │   │   │   file_batch_create_params.py
    │       │   │   │   │   file_batch_list_files_params.py
    │       │   │   │   │   file_content_response.py
    │       │   │   │   │   file_create_params.py
    │       │   │   │   │   file_list_params.py
    │       │   │   │   │   file_update_params.py
    │       │   │   │   │   vector_store_file.py
    │       │   │   │   │   vector_store_file_batch.py
    │       │   │   │   │   vector_store_file_deleted.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           file_batch_create_params.cpython-314.pyc
    │       │   │   │           file_batch_list_files_params.cpython-314.pyc
    │       │   │   │           file_content_response.cpython-314.pyc
    │       │   │   │           file_create_params.cpython-314.pyc
    │       │   │   │           file_list_params.cpython-314.pyc
    │       │   │   │           file_update_params.cpython-314.pyc
    │       │   │   │           vector_store_file.cpython-314.pyc
    │       │   │   │           vector_store_file_batch.cpython-314.pyc
    │       │   │   │           vector_store_file_deleted.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───webhooks
    │       │   │   │   │   batch_cancelled_webhook_event.py
    │       │   │   │   │   batch_completed_webhook_event.py
    │       │   │   │   │   batch_expired_webhook_event.py
    │       │   │   │   │   batch_failed_webhook_event.py
    │       │   │   │   │   eval_run_canceled_webhook_event.py
    │       │   │   │   │   eval_run_failed_webhook_event.py
    │       │   │   │   │   eval_run_succeeded_webhook_event.py
    │       │   │   │   │   fine_tuning_job_cancelled_webhook_event.py
    │       │   │   │   │   fine_tuning_job_failed_webhook_event.py
    │       │   │   │   │   fine_tuning_job_succeeded_webhook_event.py
    │       │   │   │   │   realtime_call_incoming_webhook_event.py
    │       │   │   │   │   response_cancelled_webhook_event.py
    │       │   │   │   │   response_completed_webhook_event.py
    │       │   │   │   │   response_failed_webhook_event.py
    │       │   │   │   │   response_incomplete_webhook_event.py
    │       │   │   │   │   safety_identifier_blocked_webhook_event.py
    │       │   │   │   │   unwrap_webhook_event.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           batch_cancelled_webhook_event.cpython-314.pyc
    │       │   │   │           batch_completed_webhook_event.cpython-314.pyc
    │       │   │   │           batch_expired_webhook_event.cpython-314.pyc
    │       │   │   │           batch_failed_webhook_event.cpython-314.pyc
    │       │   │   │           eval_run_canceled_webhook_event.cpython-314.pyc
    │       │   │   │           eval_run_failed_webhook_event.cpython-314.pyc
    │       │   │   │           eval_run_succeeded_webhook_event.cpython-314.pyc
    │       │   │   │           fine_tuning_job_cancelled_webhook_event.cpython-314.pyc
    │       │   │   │           fine_tuning_job_failed_webhook_event.cpython-314.pyc
    │       │   │   │           fine_tuning_job_succeeded_webhook_event.cpython-314.pyc
    │       │   │   │           realtime_call_incoming_webhook_event.cpython-314.pyc
    │       │   │   │           response_cancelled_webhook_event.cpython-314.pyc
    │       │   │   │           response_completed_webhook_event.cpython-314.pyc
    │       │   │   │           response_failed_webhook_event.cpython-314.pyc
    │       │   │   │           response_incomplete_webhook_event.cpython-314.pyc
    │       │   │   │           safety_identifier_blocked_webhook_event.cpython-314.pyc
    │       │   │   │           unwrap_webhook_event.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           audio_model.cpython-314.pyc
    │       │   │           audio_response_format.cpython-314.pyc
    │       │   │           auto_file_chunking_strategy_param.cpython-314.pyc
    │       │   │           batch.cpython-314.pyc
    │       │   │           batch_create_params.cpython-314.pyc
    │       │   │           batch_error.cpython-314.pyc
    │       │   │           batch_list_params.cpython-314.pyc
    │       │   │           batch_request_counts.cpython-314.pyc
    │       │   │           batch_usage.cpython-314.pyc
    │       │   │           chat_model.cpython-314.pyc
    │       │   │           completion.cpython-314.pyc
    │       │   │           completion_choice.cpython-314.pyc
    │       │   │           completion_create_params.cpython-314.pyc
    │       │   │           completion_usage.cpython-314.pyc
    │       │   │           container_create_params.cpython-314.pyc
    │       │   │           container_create_response.cpython-314.pyc
    │       │   │           container_list_params.cpython-314.pyc
    │       │   │           container_list_response.cpython-314.pyc
    │       │   │           container_retrieve_response.cpython-314.pyc
    │       │   │           create_embedding_response.cpython-314.pyc
    │       │   │           deleted_skill.cpython-314.pyc
    │       │   │           embedding.cpython-314.pyc
    │       │   │           embedding_create_params.cpython-314.pyc
    │       │   │           embedding_model.cpython-314.pyc
    │       │   │           eval_create_params.cpython-314.pyc
    │       │   │           eval_create_response.cpython-314.pyc
    │       │   │           eval_custom_data_source_config.cpython-314.pyc
    │       │   │           eval_delete_response.cpython-314.pyc
    │       │   │           eval_list_params.cpython-314.pyc
    │       │   │           eval_list_response.cpython-314.pyc
    │       │   │           eval_retrieve_response.cpython-314.pyc
    │       │   │           eval_stored_completions_data_source_config.cpython-314.pyc
    │       │   │           eval_update_params.cpython-314.pyc
    │       │   │           eval_update_response.cpython-314.pyc
    │       │   │           file_chunking_strategy.cpython-314.pyc
    │       │   │           file_chunking_strategy_param.cpython-314.pyc
    │       │   │           file_content.cpython-314.pyc
    │       │   │           file_create_params.cpython-314.pyc
    │       │   │           file_deleted.cpython-314.pyc
    │       │   │           file_list_params.cpython-314.pyc
    │       │   │           file_object.cpython-314.pyc
    │       │   │           file_purpose.cpython-314.pyc
    │       │   │           image.cpython-314.pyc
    │       │   │           images_response.cpython-314.pyc
    │       │   │           image_create_variation_params.cpython-314.pyc
    │       │   │           image_edit_completed_event.cpython-314.pyc
    │       │   │           image_edit_params.cpython-314.pyc
    │       │   │           image_edit_partial_image_event.cpython-314.pyc
    │       │   │           image_edit_stream_event.cpython-314.pyc
    │       │   │           image_generate_params.cpython-314.pyc
    │       │   │           image_gen_completed_event.cpython-314.pyc
    │       │   │           image_gen_partial_image_event.cpython-314.pyc
    │       │   │           image_gen_stream_event.cpython-314.pyc
    │       │   │           image_input_reference_param.cpython-314.pyc
    │       │   │           image_model.cpython-314.pyc
    │       │   │           model.cpython-314.pyc
    │       │   │           model_deleted.cpython-314.pyc
    │       │   │           moderation.cpython-314.pyc
    │       │   │           moderation_create_params.cpython-314.pyc
    │       │   │           moderation_create_response.cpython-314.pyc
    │       │   │           moderation_image_url_input_param.cpython-314.pyc
    │       │   │           moderation_model.cpython-314.pyc
    │       │   │           moderation_multi_modal_input_param.cpython-314.pyc
    │       │   │           moderation_text_input_param.cpython-314.pyc
    │       │   │           other_file_chunking_strategy_object.cpython-314.pyc
    │       │   │           skill.cpython-314.pyc
    │       │   │           skill_create_params.cpython-314.pyc
    │       │   │           skill_list.cpython-314.pyc
    │       │   │           skill_list_params.cpython-314.pyc
    │       │   │           skill_update_params.cpython-314.pyc
    │       │   │           static_file_chunking_strategy.cpython-314.pyc
    │       │   │           static_file_chunking_strategy_object.cpython-314.pyc
    │       │   │           static_file_chunking_strategy_object_param.cpython-314.pyc
    │       │   │           static_file_chunking_strategy_param.cpython-314.pyc
    │       │   │           upload.cpython-314.pyc
    │       │   │           upload_complete_params.cpython-314.pyc
    │       │   │           upload_create_params.cpython-314.pyc
    │       │   │           vector_store.cpython-314.pyc
    │       │   │           vector_store_create_params.cpython-314.pyc
    │       │   │           vector_store_deleted.cpython-314.pyc
    │       │   │           vector_store_list_params.cpython-314.pyc
    │       │   │           vector_store_search_params.cpython-314.pyc
    │       │   │           vector_store_search_response.cpython-314.pyc
    │       │   │           vector_store_update_params.cpython-314.pyc
    │       │   │           video.cpython-314.pyc
    │       │   │           video_create_character_params.cpython-314.pyc
    │       │   │           video_create_character_response.cpython-314.pyc
    │       │   │           video_create_error.cpython-314.pyc
    │       │   │           video_create_params.cpython-314.pyc
    │       │   │           video_delete_response.cpython-314.pyc
    │       │   │           video_download_content_params.cpython-314.pyc
    │       │   │           video_edit_params.cpython-314.pyc
    │       │   │           video_extend_params.cpython-314.pyc
    │       │   │           video_get_character_response.cpython-314.pyc
    │       │   │           video_list_params.cpython-314.pyc
    │       │   │           video_model.cpython-314.pyc
    │       │   │           video_model_param.cpython-314.pyc
    │       │   │           video_remix_params.cpython-314.pyc
    │       │   │           video_seconds.cpython-314.pyc
    │       │   │           video_size.cpython-314.pyc
    │       │   │           websocket_connection_options.cpython-314.pyc
    │       │   │           websocket_reconnection.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_extras
    │       │   │   │   numpy_proxy.py
    │       │   │   │   pandas_proxy.py
    │       │   │   │   sounddevice_proxy.py
    │       │   │   │   _common.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           numpy_proxy.cpython-314.pyc
    │       │   │           pandas_proxy.cpython-314.pyc
    │       │   │           sounddevice_proxy.cpython-314.pyc
    │       │   │           _common.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_utils
    │       │   │   │   _compat.py
    │       │   │   │   _datetime_parse.py
    │       │   │   │   _json.py
    │       │   │   │   _logs.py
    │       │   │   │   _path.py
    │       │   │   │   _proxy.py
    │       │   │   │   _reflection.py
    │       │   │   │   _resources_proxy.py
    │       │   │   │   _streams.py
    │       │   │   │   _sync.py
    │       │   │   │   _transform.py
    │       │   │   │   _typing.py
    │       │   │   │   _utils.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           _compat.cpython-314.pyc
    │       │   │           _datetime_parse.cpython-314.pyc
    │       │   │           _json.cpython-314.pyc
    │       │   │           _logs.cpython-314.pyc
    │       │   │           _path.cpython-314.pyc
    │       │   │           _proxy.cpython-314.pyc
    │       │   │           _reflection.cpython-314.pyc
    │       │   │           _resources_proxy.cpython-314.pyc
    │       │   │           _streams.cpython-314.pyc
    │       │   │           _sync.cpython-314.pyc
    │       │   │           _transform.cpython-314.pyc
    │       │   │           _typing.cpython-314.pyc
    │       │   │           _utils.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           pagination.cpython-314.pyc
    │       │           version.cpython-314.pyc
    │       │           _base_client.cpython-314.pyc
    │       │           _client.cpython-314.pyc
    │       │           _compat.cpython-314.pyc
    │       │           _constants.cpython-314.pyc
    │       │           _event_handler.cpython-314.pyc
    │       │           _exceptions.cpython-314.pyc
    │       │           _files.cpython-314.pyc
    │       │           _httpx2.cpython-314.pyc
    │       │           _legacy_response.cpython-314.pyc
    │       │           _models.cpython-314.pyc
    │       │           _module_client.cpython-314.pyc
    │       │           _provider.cpython-314.pyc
    │       │           _qs.cpython-314.pyc
    │       │           _resource.cpython-314.pyc
    │       │           _response.cpython-314.pyc
    │       │           _send_queue.cpython-314.pyc
    │       │           _streaming.cpython-314.pyc
    │       │           _types.cpython-314.pyc
    │       │           _version.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───openai-2.48.0.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   REQUESTED
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───pip
    │       │   │   py.typed
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │   __pip-runner__.py
    │       │   │
    │       │   ├───_internal
    │       │   │   │   build_env.py
    │       │   │   │   cache.py
    │       │   │   │   configuration.py
    │       │   │   │   exceptions.py
    │       │   │   │   main.py
    │       │   │   │   pyproject.py
    │       │   │   │   self_outdated_check.py
    │       │   │   │   wheel_builder.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   ├───cli
    │       │   │   │   │   autocompletion.py
    │       │   │   │   │   base_command.py
    │       │   │   │   │   cmdoptions.py
    │       │   │   │   │   command_context.py
    │       │   │   │   │   index_command.py
    │       │   │   │   │   main.py
    │       │   │   │   │   main_parser.py
    │       │   │   │   │   parser.py
    │       │   │   │   │   progress_bars.py
    │       │   │   │   │   req_command.py
    │       │   │   │   │   spinners.py
    │       │   │   │   │   status_codes.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           autocompletion.cpython-314.pyc
    │       │   │   │           base_command.cpython-314.pyc
    │       │   │   │           cmdoptions.cpython-314.pyc
    │       │   │   │           command_context.cpython-314.pyc
    │       │   │   │           index_command.cpython-314.pyc
    │       │   │   │           main.cpython-314.pyc
    │       │   │   │           main_parser.cpython-314.pyc
    │       │   │   │           parser.cpython-314.pyc
    │       │   │   │           progress_bars.cpython-314.pyc
    │       │   │   │           req_command.cpython-314.pyc
    │       │   │   │           spinners.cpython-314.pyc
    │       │   │   │           status_codes.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───commands
    │       │   │   │   │   cache.py
    │       │   │   │   │   check.py
    │       │   │   │   │   completion.py
    │       │   │   │   │   configuration.py
    │       │   │   │   │   debug.py
    │       │   │   │   │   download.py
    │       │   │   │   │   freeze.py
    │       │   │   │   │   hash.py
    │       │   │   │   │   help.py
    │       │   │   │   │   index.py
    │       │   │   │   │   inspect.py
    │       │   │   │   │   install.py
    │       │   │   │   │   list.py
    │       │   │   │   │   lock.py
    │       │   │   │   │   search.py
    │       │   │   │   │   show.py
    │       │   │   │   │   uninstall.py
    │       │   │   │   │   wheel.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           cache.cpython-314.pyc
    │       │   │   │           check.cpython-314.pyc
    │       │   │   │           completion.cpython-314.pyc
    │       │   │   │           configuration.cpython-314.pyc
    │       │   │   │           debug.cpython-314.pyc
    │       │   │   │           download.cpython-314.pyc
    │       │   │   │           freeze.cpython-314.pyc
    │       │   │   │           hash.cpython-314.pyc
    │       │   │   │           help.cpython-314.pyc
    │       │   │   │           index.cpython-314.pyc
    │       │   │   │           inspect.cpython-314.pyc
    │       │   │   │           install.cpython-314.pyc
    │       │   │   │           list.cpython-314.pyc
    │       │   │   │           lock.cpython-314.pyc
    │       │   │   │           search.cpython-314.pyc
    │       │   │   │           show.cpython-314.pyc
    │       │   │   │           uninstall.cpython-314.pyc
    │       │   │   │           wheel.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───distributions
    │       │   │   │   │   base.py
    │       │   │   │   │   installed.py
    │       │   │   │   │   sdist.py
    │       │   │   │   │   wheel.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           installed.cpython-314.pyc
    │       │   │   │           sdist.cpython-314.pyc
    │       │   │   │           wheel.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───index
    │       │   │   │   │   collector.py
    │       │   │   │   │   package_finder.py
    │       │   │   │   │   sources.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           collector.cpython-314.pyc
    │       │   │   │           package_finder.cpython-314.pyc
    │       │   │   │           sources.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───locations
    │       │   │   │   │   base.py
    │       │   │   │   │   _distutils.py
    │       │   │   │   │   _sysconfig.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           _distutils.cpython-314.pyc
    │       │   │   │           _sysconfig.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───metadata
    │       │   │   │   │   base.py
    │       │   │   │   │   pkg_resources.py
    │       │   │   │   │   _json.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───importlib
    │       │   │   │   │   │   _compat.py
    │       │   │   │   │   │   _dists.py
    │       │   │   │   │   │   _envs.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _compat.cpython-314.pyc
    │       │   │   │   │           _dists.cpython-314.pyc
    │       │   │   │   │           _envs.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           pkg_resources.cpython-314.pyc
    │       │   │   │           _json.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───models
    │       │   │   │   │   candidate.py
    │       │   │   │   │   direct_url.py
    │       │   │   │   │   format_control.py
    │       │   │   │   │   index.py
    │       │   │   │   │   installation_report.py
    │       │   │   │   │   link.py
    │       │   │   │   │   release_control.py
    │       │   │   │   │   scheme.py
    │       │   │   │   │   search_scope.py
    │       │   │   │   │   selection_prefs.py
    │       │   │   │   │   target_python.py
    │       │   │   │   │   wheel.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           candidate.cpython-314.pyc
    │       │   │   │           direct_url.cpython-314.pyc
    │       │   │   │           format_control.cpython-314.pyc
    │       │   │   │           index.cpython-314.pyc
    │       │   │   │           installation_report.cpython-314.pyc
    │       │   │   │           link.cpython-314.pyc
    │       │   │   │           release_control.cpython-314.pyc
    │       │   │   │           scheme.cpython-314.pyc
    │       │   │   │           search_scope.cpython-314.pyc
    │       │   │   │           selection_prefs.cpython-314.pyc
    │       │   │   │           target_python.cpython-314.pyc
    │       │   │   │           wheel.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───network
    │       │   │   │   │   auth.py
    │       │   │   │   │   cache.py
    │       │   │   │   │   download.py
    │       │   │   │   │   lazy_wheel.py
    │       │   │   │   │   session.py
    │       │   │   │   │   utils.py
    │       │   │   │   │   xmlrpc.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           auth.cpython-314.pyc
    │       │   │   │           cache.cpython-314.pyc
    │       │   │   │           download.cpython-314.pyc
    │       │   │   │           lazy_wheel.cpython-314.pyc
    │       │   │   │           session.cpython-314.pyc
    │       │   │   │           utils.cpython-314.pyc
    │       │   │   │           xmlrpc.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───operations
    │       │   │   │   │   check.py
    │       │   │   │   │   freeze.py
    │       │   │   │   │   prepare.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───build
    │       │   │   │   │   │   build_tracker.py
    │       │   │   │   │   │   metadata.py
    │       │   │   │   │   │   metadata_editable.py
    │       │   │   │   │   │   wheel.py
    │       │   │   │   │   │   wheel_editable.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           build_tracker.cpython-314.pyc
    │       │   │   │   │           metadata.cpython-314.pyc
    │       │   │   │   │           metadata_editable.cpython-314.pyc
    │       │   │   │   │           wheel.cpython-314.pyc
    │       │   │   │   │           wheel_editable.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───install
    │       │   │   │   │   │   wheel.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           wheel.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           check.cpython-314.pyc
    │       │   │   │           freeze.cpython-314.pyc
    │       │   │   │           prepare.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───req
    │       │   │   │   │   constructors.py
    │       │   │   │   │   pep723.py
    │       │   │   │   │   req_dependency_group.py
    │       │   │   │   │   req_file.py
    │       │   │   │   │   req_install.py
    │       │   │   │   │   req_set.py
    │       │   │   │   │   req_uninstall.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           constructors.cpython-314.pyc
    │       │   │   │           pep723.cpython-314.pyc
    │       │   │   │           req_dependency_group.cpython-314.pyc
    │       │   │   │           req_file.cpython-314.pyc
    │       │   │   │           req_install.cpython-314.pyc
    │       │   │   │           req_set.cpython-314.pyc
    │       │   │   │           req_uninstall.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───resolution
    │       │   │   │   │   base.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───legacy
    │       │   │   │   │   │   resolver.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           resolver.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───resolvelib
    │       │   │   │   │   │   base.py
    │       │   │   │   │   │   candidates.py
    │       │   │   │   │   │   factory.py
    │       │   │   │   │   │   found_candidates.py
    │       │   │   │   │   │   provider.py
    │       │   │   │   │   │   reporter.py
    │       │   │   │   │   │   requirements.py
    │       │   │   │   │   │   resolver.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           base.cpython-314.pyc
    │       │   │   │   │           candidates.cpython-314.pyc
    │       │   │   │   │           factory.cpython-314.pyc
    │       │   │   │   │           found_candidates.cpython-314.pyc
    │       │   │   │   │           provider.cpython-314.pyc
    │       │   │   │   │           reporter.cpython-314.pyc
    │       │   │   │   │           requirements.cpython-314.pyc
    │       │   │   │   │           resolver.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───utils
    │       │   │   │   │   appdirs.py
    │       │   │   │   │   compat.py
    │       │   │   │   │   compatibility_tags.py
    │       │   │   │   │   datetime.py
    │       │   │   │   │   deprecation.py
    │       │   │   │   │   direct_url_helpers.py
    │       │   │   │   │   egg_link.py
    │       │   │   │   │   entrypoints.py
    │       │   │   │   │   filesystem.py
    │       │   │   │   │   filetypes.py
    │       │   │   │   │   glibc.py
    │       │   │   │   │   hashes.py
    │       │   │   │   │   logging.py
    │       │   │   │   │   misc.py
    │       │   │   │   │   packaging.py
    │       │   │   │   │   pylock.py
    │       │   │   │   │   retry.py
    │       │   │   │   │   subprocess.py
    │       │   │   │   │   temp_dir.py
    │       │   │   │   │   unpacking.py
    │       │   │   │   │   urls.py
    │       │   │   │   │   virtualenv.py
    │       │   │   │   │   wheel.py
    │       │   │   │   │   _jaraco_text.py
    │       │   │   │   │   _log.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           appdirs.cpython-314.pyc
    │       │   │   │           compat.cpython-314.pyc
    │       │   │   │           compatibility_tags.cpython-314.pyc
    │       │   │   │           datetime.cpython-314.pyc
    │       │   │   │           deprecation.cpython-314.pyc
    │       │   │   │           direct_url_helpers.cpython-314.pyc
    │       │   │   │           egg_link.cpython-314.pyc
    │       │   │   │           entrypoints.cpython-314.pyc
    │       │   │   │           filesystem.cpython-314.pyc
    │       │   │   │           filetypes.cpython-314.pyc
    │       │   │   │           glibc.cpython-314.pyc
    │       │   │   │           hashes.cpython-314.pyc
    │       │   │   │           logging.cpython-314.pyc
    │       │   │   │           misc.cpython-314.pyc
    │       │   │   │           packaging.cpython-314.pyc
    │       │   │   │           pylock.cpython-314.pyc
    │       │   │   │           retry.cpython-314.pyc
    │       │   │   │           subprocess.cpython-314.pyc
    │       │   │   │           temp_dir.cpython-314.pyc
    │       │   │   │           unpacking.cpython-314.pyc
    │       │   │   │           urls.cpython-314.pyc
    │       │   │   │           virtualenv.cpython-314.pyc
    │       │   │   │           wheel.cpython-314.pyc
    │       │   │   │           _jaraco_text.cpython-314.pyc
    │       │   │   │           _log.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───vcs
    │       │   │   │   │   bazaar.py
    │       │   │   │   │   git.py
    │       │   │   │   │   mercurial.py
    │       │   │   │   │   subversion.py
    │       │   │   │   │   versioncontrol.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           bazaar.cpython-314.pyc
    │       │   │   │           git.cpython-314.pyc
    │       │   │   │           mercurial.cpython-314.pyc
    │       │   │   │           subversion.cpython-314.pyc
    │       │   │   │           versioncontrol.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           build_env.cpython-314.pyc
    │       │   │           cache.cpython-314.pyc
    │       │   │           configuration.cpython-314.pyc
    │       │   │           exceptions.cpython-314.pyc
    │       │   │           main.cpython-314.pyc
    │       │   │           pyproject.cpython-314.pyc
    │       │   │           self_outdated_check.cpython-314.pyc
    │       │   │           wheel_builder.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_vendor
    │       │   │   │   README.rst
    │       │   │   │   vendor.txt
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   ├───cachecontrol
    │       │   │   │   │   adapter.py
    │       │   │   │   │   cache.py
    │       │   │   │   │   controller.py
    │       │   │   │   │   filewrapper.py
    │       │   │   │   │   heuristics.py
    │       │   │   │   │   LICENSE.txt
    │       │   │   │   │   py.typed
    │       │   │   │   │   serialize.py
    │       │   │   │   │   wrapper.py
    │       │   │   │   │   _cmd.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───caches
    │       │   │   │   │   │   file_cache.py
    │       │   │   │   │   │   redis_cache.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           file_cache.cpython-314.pyc
    │       │   │   │   │           redis_cache.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           adapter.cpython-314.pyc
    │       │   │   │           cache.cpython-314.pyc
    │       │   │   │           controller.cpython-314.pyc
    │       │   │   │           filewrapper.cpython-314.pyc
    │       │   │   │           heuristics.cpython-314.pyc
    │       │   │   │           serialize.cpython-314.pyc
    │       │   │   │           wrapper.cpython-314.pyc
    │       │   │   │           _cmd.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───certifi
    │       │   │   │   │   cacert.pem
    │       │   │   │   │   core.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           core.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───distlib
    │       │   │   │   │   compat.py
    │       │   │   │   │   LICENSE.txt
    │       │   │   │   │   resources.py
    │       │   │   │   │   scripts.py
    │       │   │   │   │   t32.exe
    │       │   │   │   │   t64-arm.exe
    │       │   │   │   │   t64.exe
    │       │   │   │   │   util.py
    │       │   │   │   │   w32.exe
    │       │   │   │   │   w64-arm.exe
    │       │   │   │   │   w64.exe
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           compat.cpython-314.pyc
    │       │   │   │           resources.cpython-314.pyc
    │       │   │   │           scripts.cpython-314.pyc
    │       │   │   │           util.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───distro
    │       │   │   │   │   distro.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           distro.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───idna
    │       │   │   │   │   codec.py
    │       │   │   │   │   compat.py
    │       │   │   │   │   core.py
    │       │   │   │   │   idnadata.py
    │       │   │   │   │   intranges.py
    │       │   │   │   │   LICENSE.md
    │       │   │   │   │   package_data.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   uts46data.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           codec.cpython-314.pyc
    │       │   │   │           compat.cpython-314.pyc
    │       │   │   │           core.cpython-314.pyc
    │       │   │   │           idnadata.cpython-314.pyc
    │       │   │   │           intranges.cpython-314.pyc
    │       │   │   │           package_data.cpython-314.pyc
    │       │   │   │           uts46data.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───msgpack
    │       │   │   │   │   COPYING
    │       │   │   │   │   exceptions.py
    │       │   │   │   │   ext.py
    │       │   │   │   │   fallback.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           exceptions.cpython-314.pyc
    │       │   │   │           ext.cpython-314.pyc
    │       │   │   │           fallback.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───packaging
    │       │   │   │   │   dependency_groups.py
    │       │   │   │   │   direct_url.py
    │       │   │   │   │   errors.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   LICENSE.APACHE
    │       │   │   │   │   LICENSE.BSD
    │       │   │   │   │   markers.py
    │       │   │   │   │   metadata.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   pylock.py
    │       │   │   │   │   requirements.py
    │       │   │   │   │   specifiers.py
    │       │   │   │   │   tags.py
    │       │   │   │   │   utils.py
    │       │   │   │   │   version.py
    │       │   │   │   │   _elffile.py
    │       │   │   │   │   _manylinux.py
    │       │   │   │   │   _musllinux.py
    │       │   │   │   │   _parser.py
    │       │   │   │   │   _structures.py
    │       │   │   │   │   _tokenizer.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───licenses
    │       │   │   │   │   │   _spdx.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _spdx.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           dependency_groups.cpython-314.pyc
    │       │   │   │           direct_url.cpython-314.pyc
    │       │   │   │           errors.cpython-314.pyc
    │       │   │   │           markers.cpython-314.pyc
    │       │   │   │           metadata.cpython-314.pyc
    │       │   │   │           pylock.cpython-314.pyc
    │       │   │   │           requirements.cpython-314.pyc
    │       │   │   │           specifiers.cpython-314.pyc
    │       │   │   │           tags.cpython-314.pyc
    │       │   │   │           utils.cpython-314.pyc
    │       │   │   │           version.cpython-314.pyc
    │       │   │   │           _elffile.cpython-314.pyc
    │       │   │   │           _manylinux.cpython-314.pyc
    │       │   │   │           _musllinux.cpython-314.pyc
    │       │   │   │           _parser.cpython-314.pyc
    │       │   │   │           _structures.cpython-314.pyc
    │       │   │   │           _tokenizer.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───pkg_resources
    │       │   │   │   │   LICENSE
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───platformdirs
    │       │   │   │   │   android.py
    │       │   │   │   │   api.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   macos.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   unix.py
    │       │   │   │   │   version.py
    │       │   │   │   │   windows.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           android.cpython-314.pyc
    │       │   │   │           api.cpython-314.pyc
    │       │   │   │           macos.cpython-314.pyc
    │       │   │   │           unix.cpython-314.pyc
    │       │   │   │           version.cpython-314.pyc
    │       │   │   │           windows.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───pygments
    │       │   │   │   │   console.py
    │       │   │   │   │   filter.py
    │       │   │   │   │   formatter.py
    │       │   │   │   │   lexer.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   modeline.py
    │       │   │   │   │   plugin.py
    │       │   │   │   │   regexopt.py
    │       │   │   │   │   scanner.py
    │       │   │   │   │   sphinxext.py
    │       │   │   │   │   style.py
    │       │   │   │   │   token.py
    │       │   │   │   │   unistring.py
    │       │   │   │   │   util.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   ├───filters
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───formatters
    │       │   │   │   │   │   _mapping.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _mapping.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───lexers
    │       │   │   │   │   │   python.py
    │       │   │   │   │   │   _mapping.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           python.cpython-314.pyc
    │       │   │   │   │           _mapping.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───styles
    │       │   │   │   │   │   _mapping.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _mapping.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           console.cpython-314.pyc
    │       │   │   │           filter.cpython-314.pyc
    │       │   │   │           formatter.cpython-314.pyc
    │       │   │   │           lexer.cpython-314.pyc
    │       │   │   │           modeline.cpython-314.pyc
    │       │   │   │           plugin.cpython-314.pyc
    │       │   │   │           regexopt.cpython-314.pyc
    │       │   │   │           scanner.cpython-314.pyc
    │       │   │   │           sphinxext.cpython-314.pyc
    │       │   │   │           style.cpython-314.pyc
    │       │   │   │           token.cpython-314.pyc
    │       │   │   │           unistring.cpython-314.pyc
    │       │   │   │           util.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───pyproject_hooks
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   _impl.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───_in_process
    │       │   │   │   │   │   _in_process.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _in_process.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _impl.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───requests
    │       │   │   │   │   adapters.py
    │       │   │   │   │   api.py
    │       │   │   │   │   auth.py
    │       │   │   │   │   certs.py
    │       │   │   │   │   compat.py
    │       │   │   │   │   cookies.py
    │       │   │   │   │   exceptions.py
    │       │   │   │   │   help.py
    │       │   │   │   │   hooks.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   models.py
    │       │   │   │   │   packages.py
    │       │   │   │   │   sessions.py
    │       │   │   │   │   status_codes.py
    │       │   │   │   │   structures.py
    │       │   │   │   │   utils.py
    │       │   │   │   │   _internal_utils.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __version__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           adapters.cpython-314.pyc
    │       │   │   │           api.cpython-314.pyc
    │       │   │   │           auth.cpython-314.pyc
    │       │   │   │           certs.cpython-314.pyc
    │       │   │   │           compat.cpython-314.pyc
    │       │   │   │           cookies.cpython-314.pyc
    │       │   │   │           exceptions.cpython-314.pyc
    │       │   │   │           help.cpython-314.pyc
    │       │   │   │           hooks.cpython-314.pyc
    │       │   │   │           models.cpython-314.pyc
    │       │   │   │           packages.cpython-314.pyc
    │       │   │   │           sessions.cpython-314.pyc
    │       │   │   │           status_codes.cpython-314.pyc
    │       │   │   │           structures.cpython-314.pyc
    │       │   │   │           utils.cpython-314.pyc
    │       │   │   │           _internal_utils.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __version__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───resolvelib
    │       │   │   │   │   LICENSE
    │       │   │   │   │   providers.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   reporters.py
    │       │   │   │   │   structs.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───resolvers
    │       │   │   │   │   │   abstract.py
    │       │   │   │   │   │   criterion.py
    │       │   │   │   │   │   exceptions.py
    │       │   │   │   │   │   resolution.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           abstract.cpython-314.pyc
    │       │   │   │   │           criterion.cpython-314.pyc
    │       │   │   │   │           exceptions.cpython-314.pyc
    │       │   │   │   │           resolution.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           providers.cpython-314.pyc
    │       │   │   │           reporters.cpython-314.pyc
    │       │   │   │           structs.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───rich
    │       │   │   │   │   abc.py
    │       │   │   │   │   align.py
    │       │   │   │   │   ansi.py
    │       │   │   │   │   bar.py
    │       │   │   │   │   box.py
    │       │   │   │   │   cells.py
    │       │   │   │   │   color.py
    │       │   │   │   │   color_triplet.py
    │       │   │   │   │   columns.py
    │       │   │   │   │   console.py
    │       │   │   │   │   constrain.py
    │       │   │   │   │   containers.py
    │       │   │   │   │   control.py
    │       │   │   │   │   default_styles.py
    │       │   │   │   │   diagnose.py
    │       │   │   │   │   emoji.py
    │       │   │   │   │   errors.py
    │       │   │   │   │   filesize.py
    │       │   │   │   │   file_proxy.py
    │       │   │   │   │   highlighter.py
    │       │   │   │   │   json.py
    │       │   │   │   │   jupyter.py
    │       │   │   │   │   layout.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   live.py
    │       │   │   │   │   live_render.py
    │       │   │   │   │   logging.py
    │       │   │   │   │   markup.py
    │       │   │   │   │   measure.py
    │       │   │   │   │   padding.py
    │       │   │   │   │   pager.py
    │       │   │   │   │   palette.py
    │       │   │   │   │   panel.py
    │       │   │   │   │   pretty.py
    │       │   │   │   │   progress.py
    │       │   │   │   │   progress_bar.py
    │       │   │   │   │   prompt.py
    │       │   │   │   │   protocol.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   region.py
    │       │   │   │   │   repr.py
    │       │   │   │   │   rule.py
    │       │   │   │   │   scope.py
    │       │   │   │   │   screen.py
    │       │   │   │   │   segment.py
    │       │   │   │   │   spinner.py
    │       │   │   │   │   status.py
    │       │   │   │   │   style.py
    │       │   │   │   │   styled.py
    │       │   │   │   │   syntax.py
    │       │   │   │   │   table.py
    │       │   │   │   │   terminal_theme.py
    │       │   │   │   │   text.py
    │       │   │   │   │   theme.py
    │       │   │   │   │   themes.py
    │       │   │   │   │   traceback.py
    │       │   │   │   │   tree.py
    │       │   │   │   │   _cell_widths.py
    │       │   │   │   │   _emoji_codes.py
    │       │   │   │   │   _emoji_replace.py
    │       │   │   │   │   _export_format.py
    │       │   │   │   │   _extension.py
    │       │   │   │   │   _fileno.py
    │       │   │   │   │   _inspect.py
    │       │   │   │   │   _log_render.py
    │       │   │   │   │   _loop.py
    │       │   │   │   │   _null_file.py
    │       │   │   │   │   _palettes.py
    │       │   │   │   │   _pick.py
    │       │   │   │   │   _ratio.py
    │       │   │   │   │   _spinners.py
    │       │   │   │   │   _stack.py
    │       │   │   │   │   _timer.py
    │       │   │   │   │   _win32_console.py
    │       │   │   │   │   _windows.py
    │       │   │   │   │   _windows_renderer.py
    │       │   │   │   │   _wrap.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           abc.cpython-314.pyc
    │       │   │   │           align.cpython-314.pyc
    │       │   │   │           ansi.cpython-314.pyc
    │       │   │   │           bar.cpython-314.pyc
    │       │   │   │           box.cpython-314.pyc
    │       │   │   │           cells.cpython-314.pyc
    │       │   │   │           color.cpython-314.pyc
    │       │   │   │           color_triplet.cpython-314.pyc
    │       │   │   │           columns.cpython-314.pyc
    │       │   │   │           console.cpython-314.pyc
    │       │   │   │           constrain.cpython-314.pyc
    │       │   │   │           containers.cpython-314.pyc
    │       │   │   │           control.cpython-314.pyc
    │       │   │   │           default_styles.cpython-314.pyc
    │       │   │   │           diagnose.cpython-314.pyc
    │       │   │   │           emoji.cpython-314.pyc
    │       │   │   │           errors.cpython-314.pyc
    │       │   │   │           filesize.cpython-314.pyc
    │       │   │   │           file_proxy.cpython-314.pyc
    │       │   │   │           highlighter.cpython-314.pyc
    │       │   │   │           json.cpython-314.pyc
    │       │   │   │           jupyter.cpython-314.pyc
    │       │   │   │           layout.cpython-314.pyc
    │       │   │   │           live.cpython-314.pyc
    │       │   │   │           live_render.cpython-314.pyc
    │       │   │   │           logging.cpython-314.pyc
    │       │   │   │           markup.cpython-314.pyc
    │       │   │   │           measure.cpython-314.pyc
    │       │   │   │           padding.cpython-314.pyc
    │       │   │   │           pager.cpython-314.pyc
    │       │   │   │           palette.cpython-314.pyc
    │       │   │   │           panel.cpython-314.pyc
    │       │   │   │           pretty.cpython-314.pyc
    │       │   │   │           progress.cpython-314.pyc
    │       │   │   │           progress_bar.cpython-314.pyc
    │       │   │   │           prompt.cpython-314.pyc
    │       │   │   │           protocol.cpython-314.pyc
    │       │   │   │           region.cpython-314.pyc
    │       │   │   │           repr.cpython-314.pyc
    │       │   │   │           rule.cpython-314.pyc
    │       │   │   │           scope.cpython-314.pyc
    │       │   │   │           screen.cpython-314.pyc
    │       │   │   │           segment.cpython-314.pyc
    │       │   │   │           spinner.cpython-314.pyc
    │       │   │   │           status.cpython-314.pyc
    │       │   │   │           style.cpython-314.pyc
    │       │   │   │           styled.cpython-314.pyc
    │       │   │   │           syntax.cpython-314.pyc
    │       │   │   │           table.cpython-314.pyc
    │       │   │   │           terminal_theme.cpython-314.pyc
    │       │   │   │           text.cpython-314.pyc
    │       │   │   │           theme.cpython-314.pyc
    │       │   │   │           themes.cpython-314.pyc
    │       │   │   │           traceback.cpython-314.pyc
    │       │   │   │           tree.cpython-314.pyc
    │       │   │   │           _cell_widths.cpython-314.pyc
    │       │   │   │           _emoji_codes.cpython-314.pyc
    │       │   │   │           _emoji_replace.cpython-314.pyc
    │       │   │   │           _export_format.cpython-314.pyc
    │       │   │   │           _extension.cpython-314.pyc
    │       │   │   │           _fileno.cpython-314.pyc
    │       │   │   │           _inspect.cpython-314.pyc
    │       │   │   │           _log_render.cpython-314.pyc
    │       │   │   │           _loop.cpython-314.pyc
    │       │   │   │           _null_file.cpython-314.pyc
    │       │   │   │           _palettes.cpython-314.pyc
    │       │   │   │           _pick.cpython-314.pyc
    │       │   │   │           _ratio.cpython-314.pyc
    │       │   │   │           _spinners.cpython-314.pyc
    │       │   │   │           _stack.cpython-314.pyc
    │       │   │   │           _timer.cpython-314.pyc
    │       │   │   │           _win32_console.cpython-314.pyc
    │       │   │   │           _windows.cpython-314.pyc
    │       │   │   │           _windows_renderer.cpython-314.pyc
    │       │   │   │           _wrap.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───tomli
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   _parser.py
    │       │   │   │   │   _re.py
    │       │   │   │   │   _types.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _parser.cpython-314.pyc
    │       │   │   │           _re.cpython-314.pyc
    │       │   │   │           _types.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───tomli_w
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   _writer.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _writer.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───truststore
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   _api.py
    │       │   │   │   │   _macos.py
    │       │   │   │   │   _openssl.py
    │       │   │   │   │   _ssl_constants.py
    │       │   │   │   │   _windows.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _api.cpython-314.pyc
    │       │   │   │           _macos.cpython-314.pyc
    │       │   │   │           _openssl.cpython-314.pyc
    │       │   │   │           _ssl_constants.cpython-314.pyc
    │       │   │   │           _windows.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───urllib3
    │       │   │   │   │   connection.py
    │       │   │   │   │   connectionpool.py
    │       │   │   │   │   exceptions.py
    │       │   │   │   │   fields.py
    │       │   │   │   │   filepost.py
    │       │   │   │   │   LICENSE.txt
    │       │   │   │   │   poolmanager.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   response.py
    │       │   │   │   │   _base_connection.py
    │       │   │   │   │   _collections.py
    │       │   │   │   │   _request_methods.py
    │       │   │   │   │   _version.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───contrib
    │       │   │   │   │   │   pyopenssl.py
    │       │   │   │   │   │   socks.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   ├───emscripten
    │       │   │   │   │   │   │   connection.py
    │       │   │   │   │   │   │   emscripten_fetch_worker.js
    │       │   │   │   │   │   │   fetch.py
    │       │   │   │   │   │   │   request.py
    │       │   │   │   │   │   │   response.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           connection.cpython-314.pyc
    │       │   │   │   │   │           fetch.cpython-314.pyc
    │       │   │   │   │   │           request.cpython-314.pyc
    │       │   │   │   │   │           response.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           pyopenssl.cpython-314.pyc
    │       │   │   │   │           socks.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───http2
    │       │   │   │   │   │   connection.py
    │       │   │   │   │   │   probe.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           connection.cpython-314.pyc
    │       │   │   │   │           probe.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───util
    │       │   │   │   │   │   connection.py
    │       │   │   │   │   │   proxy.py
    │       │   │   │   │   │   request.py
    │       │   │   │   │   │   response.py
    │       │   │   │   │   │   retry.py
    │       │   │   │   │   │   ssltransport.py
    │       │   │   │   │   │   ssl_.py
    │       │   │   │   │   │   ssl_match_hostname.py
    │       │   │   │   │   │   timeout.py
    │       │   │   │   │   │   url.py
    │       │   │   │   │   │   util.py
    │       │   │   │   │   │   wait.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           connection.cpython-314.pyc
    │       │   │   │   │           proxy.cpython-314.pyc
    │       │   │   │   │           request.cpython-314.pyc
    │       │   │   │   │           response.cpython-314.pyc
    │       │   │   │   │           retry.cpython-314.pyc
    │       │   │   │   │           ssltransport.cpython-314.pyc
    │       │   │   │   │           ssl_.cpython-314.pyc
    │       │   │   │   │           ssl_match_hostname.cpython-314.pyc
    │       │   │   │   │           timeout.cpython-314.pyc
    │       │   │   │   │           url.cpython-314.pyc
    │       │   │   │   │           util.cpython-314.pyc
    │       │   │   │   │           wait.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           connection.cpython-314.pyc
    │       │   │   │           connectionpool.cpython-314.pyc
    │       │   │   │           exceptions.cpython-314.pyc
    │       │   │   │           fields.cpython-314.pyc
    │       │   │   │           filepost.cpython-314.pyc
    │       │   │   │           poolmanager.cpython-314.pyc
    │       │   │   │           response.cpython-314.pyc
    │       │   │   │           _base_connection.cpython-314.pyc
    │       │   │   │           _collections.cpython-314.pyc
    │       │   │   │           _request_methods.cpython-314.pyc
    │       │   │   │           _version.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │           __pip-runner__.cpython-314.pyc
    │       │
    │       ├───pip-26.1.2.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   REQUESTED
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │       │   AUTHORS.txt
    │       │       │   LICENSE.txt
    │       │       │
    │       │       └───src
    │       │           └───pip
    │       │               └───_vendor
    │       │                   ├───cachecontrol
    │       │                   │       LICENSE.txt
    │       │                   │
    │       │                   ├───certifi
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───distlib
    │       │                   │       LICENSE.txt
    │       │                   │
    │       │                   ├───distro
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───idna
    │       │                   │       LICENSE.md
    │       │                   │
    │       │                   ├───msgpack
    │       │                   │       COPYING
    │       │                   │
    │       │                   ├───packaging
    │       │                   │       LICENSE
    │       │                   │       LICENSE.APACHE
    │       │                   │       LICENSE.BSD
    │       │                   │
    │       │                   ├───pkg_resources
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───platformdirs
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───pygments
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───pyproject_hooks
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───requests
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───resolvelib
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───rich
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───tomli
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───tomli_w
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───truststore
    │       │                   │       LICENSE
    │       │                   │
    │       │                   └───urllib3
    │       │                           LICENSE.txt
    │       │
    │       ├───pydantic
    │       │   │   aliases.py
    │       │   │   alias_generators.py
    │       │   │   annotated_handlers.py
    │       │   │   class_validators.py
    │       │   │   color.py
    │       │   │   config.py
    │       │   │   dataclasses.py
    │       │   │   datetime_parse.py
    │       │   │   decorator.py
    │       │   │   env_settings.py
    │       │   │   errors.py
    │       │   │   error_wrappers.py
    │       │   │   fields.py
    │       │   │   functional_serializers.py
    │       │   │   functional_validators.py
    │       │   │   generics.py
    │       │   │   json.py
    │       │   │   json_schema.py
    │       │   │   main.py
    │       │   │   mypy.py
    │       │   │   networks.py
    │       │   │   parse.py
    │       │   │   py.typed
    │       │   │   root_model.py
    │       │   │   schema.py
    │       │   │   tools.py
    │       │   │   types.py
    │       │   │   type_adapter.py
    │       │   │   typing.py
    │       │   │   utils.py
    │       │   │   validate_call_decorator.py
    │       │   │   validators.py
    │       │   │   version.py
    │       │   │   warnings.py
    │       │   │   _migration.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───deprecated
    │       │   │   │   class_validators.py
    │       │   │   │   config.py
    │       │   │   │   copy_internals.py
    │       │   │   │   decorator.py
    │       │   │   │   json.py
    │       │   │   │   parse.py
    │       │   │   │   tools.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           class_validators.cpython-314.pyc
    │       │   │           config.cpython-314.pyc
    │       │   │           copy_internals.cpython-314.pyc
    │       │   │           decorator.cpython-314.pyc
    │       │   │           json.cpython-314.pyc
    │       │   │           parse.cpython-314.pyc
    │       │   │           tools.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───experimental
    │       │   │   │   arguments_schema.py
    │       │   │   │   missing_sentinel.py
    │       │   │   │   pipeline.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           arguments_schema.cpython-314.pyc
    │       │   │           missing_sentinel.cpython-314.pyc
    │       │   │           pipeline.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───plugin
    │       │   │   │   _loader.py
    │       │   │   │   _schema_validator.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           _loader.cpython-314.pyc
    │       │   │           _schema_validator.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───v1
    │       │   │   │   annotated_types.py
    │       │   │   │   class_validators.py
    │       │   │   │   color.py
    │       │   │   │   config.py
    │       │   │   │   dataclasses.py
    │       │   │   │   datetime_parse.py
    │       │   │   │   decorator.py
    │       │   │   │   env_settings.py
    │       │   │   │   errors.py
    │       │   │   │   error_wrappers.py
    │       │   │   │   fields.py
    │       │   │   │   generics.py
    │       │   │   │   json.py
    │       │   │   │   main.py
    │       │   │   │   mypy.py
    │       │   │   │   networks.py
    │       │   │   │   parse.py
    │       │   │   │   py.typed
    │       │   │   │   schema.py
    │       │   │   │   tools.py
    │       │   │   │   types.py
    │       │   │   │   typing.py
    │       │   │   │   utils.py
    │       │   │   │   validators.py
    │       │   │   │   version.py
    │       │   │   │   _hypothesis_plugin.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           annotated_types.cpython-314.pyc
    │       │   │           class_validators.cpython-314.pyc
    │       │   │           color.cpython-314.pyc
    │       │   │           config.cpython-314.pyc
    │       │   │           dataclasses.cpython-314.pyc
    │       │   │           datetime_parse.cpython-314.pyc
    │       │   │           decorator.cpython-314.pyc
    │       │   │           env_settings.cpython-314.pyc
    │       │   │           errors.cpython-314.pyc
    │       │   │           error_wrappers.cpython-314.pyc
    │       │   │           fields.cpython-314.pyc
    │       │   │           generics.cpython-314.pyc
    │       │   │           json.cpython-314.pyc
    │       │   │           main.cpython-314.pyc
    │       │   │           mypy.cpython-314.pyc
    │       │   │           networks.cpython-314.pyc
    │       │   │           parse.cpython-314.pyc
    │       │   │           schema.cpython-314.pyc
    │       │   │           tools.cpython-314.pyc
    │       │   │           types.cpython-314.pyc
    │       │   │           typing.cpython-314.pyc
    │       │   │           utils.cpython-314.pyc
    │       │   │           validators.cpython-314.pyc
    │       │   │           version.cpython-314.pyc
    │       │   │           _hypothesis_plugin.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_internal
    │       │   │   │   _config.py
    │       │   │   │   _core_metadata.py
    │       │   │   │   _core_utils.py
    │       │   │   │   _dataclasses.py
    │       │   │   │   _decorators.py
    │       │   │   │   _decorators_v1.py
    │       │   │   │   _discriminated_union.py
    │       │   │   │   _docs_extraction.py
    │       │   │   │   _fields.py
    │       │   │   │   _forward_ref.py
    │       │   │   │   _generate_schema.py
    │       │   │   │   _generics.py
    │       │   │   │   _git.py
    │       │   │   │   _import_utils.py
    │       │   │   │   _internal_dataclass.py
    │       │   │   │   _known_annotated_metadata.py
    │       │   │   │   _mock_val_ser.py
    │       │   │   │   _model_construction.py
    │       │   │   │   _namespace_utils.py
    │       │   │   │   _repr.py
    │       │   │   │   _schema_gather.py
    │       │   │   │   _schema_generation_shared.py
    │       │   │   │   _serializers.py
    │       │   │   │   _signature.py
    │       │   │   │   _typing_extra.py
    │       │   │   │   _utils.py
    │       │   │   │   _validate_call.py
    │       │   │   │   _validators.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           _config.cpython-314.pyc
    │       │   │           _core_metadata.cpython-314.pyc
    │       │   │           _core_utils.cpython-314.pyc
    │       │   │           _dataclasses.cpython-314.pyc
    │       │   │           _decorators.cpython-314.pyc
    │       │   │           _decorators_v1.cpython-314.pyc
    │       │   │           _discriminated_union.cpython-314.pyc
    │       │   │           _docs_extraction.cpython-314.pyc
    │       │   │           _fields.cpython-314.pyc
    │       │   │           _forward_ref.cpython-314.pyc
    │       │   │           _generate_schema.cpython-314.pyc
    │       │   │           _generics.cpython-314.pyc
    │       │   │           _git.cpython-314.pyc
    │       │   │           _import_utils.cpython-314.pyc
    │       │   │           _internal_dataclass.cpython-314.pyc
    │       │   │           _known_annotated_metadata.cpython-314.pyc
    │       │   │           _mock_val_ser.cpython-314.pyc
    │       │   │           _model_construction.cpython-314.pyc
    │       │   │           _namespace_utils.cpython-314.pyc
    │       │   │           _repr.cpython-314.pyc
    │       │   │           _schema_gather.cpython-314.pyc
    │       │   │           _schema_generation_shared.cpython-314.pyc
    │       │   │           _serializers.cpython-314.pyc
    │       │   │           _signature.cpython-314.pyc
    │       │   │           _typing_extra.cpython-314.pyc
    │       │   │           _utils.cpython-314.pyc
    │       │   │           _validate_call.cpython-314.pyc
    │       │   │           _validators.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           aliases.cpython-314.pyc
    │       │           alias_generators.cpython-314.pyc
    │       │           annotated_handlers.cpython-314.pyc
    │       │           class_validators.cpython-314.pyc
    │       │           color.cpython-314.pyc
    │       │           config.cpython-314.pyc
    │       │           dataclasses.cpython-314.pyc
    │       │           datetime_parse.cpython-314.pyc
    │       │           decorator.cpython-314.pyc
    │       │           env_settings.cpython-314.pyc
    │       │           errors.cpython-314.pyc
    │       │           error_wrappers.cpython-314.pyc
    │       │           fields.cpython-314.pyc
    │       │           functional_serializers.cpython-314.pyc
    │       │           functional_validators.cpython-314.pyc
    │       │           generics.cpython-314.pyc
    │       │           json.cpython-314.pyc
    │       │           json_schema.cpython-314.pyc
    │       │           main.cpython-314.pyc
    │       │           mypy.cpython-314.pyc
    │       │           networks.cpython-314.pyc
    │       │           parse.cpython-314.pyc
    │       │           root_model.cpython-314.pyc
    │       │           schema.cpython-314.pyc
    │       │           tools.cpython-314.pyc
    │       │           types.cpython-314.pyc
    │       │           type_adapter.cpython-314.pyc
    │       │           typing.cpython-314.pyc
    │       │           utils.cpython-314.pyc
    │       │           validate_call_decorator.cpython-314.pyc
    │       │           validators.cpython-314.pyc
    │       │           version.cpython-314.pyc
    │       │           warnings.cpython-314.pyc
    │       │           _migration.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───pydantic-2.13.4.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───pydantic_core
    │       │   │   core_schema.py
    │       │   │   py.typed
    │       │   │   _pydantic_core.cp314-win_amd64.pyd
    │       │   │   _pydantic_core.pyi
    │       │   │   __init__.py
    │       │   │
    │       │   └───__pycache__
    │       │           core_schema.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───pydantic_core-2.46.4.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   ├───licenses
    │       │   │       LICENSE
    │       │   │
    │       │   └───sboms
    │       │           pydantic-core.cyclonedx.json
    │       │
    │       ├───requests
    │       │   │   adapters.py
    │       │   │   api.py
    │       │   │   auth.py
    │       │   │   certs.py
    │       │   │   compat.py
    │       │   │   cookies.py
    │       │   │   exceptions.py
    │       │   │   help.py
    │       │   │   hooks.py
    │       │   │   models.py
    │       │   │   packages.py
    │       │   │   py.typed
    │       │   │   sessions.py
    │       │   │   status_codes.py
    │       │   │   structures.py
    │       │   │   utils.py
    │       │   │   _internal_utils.py
    │       │   │   _types.py
    │       │   │   __init__.py
    │       │   │   __version__.py
    │       │   │
    │       │   └───__pycache__
    │       │           adapters.cpython-314.pyc
    │       │           api.cpython-314.pyc
    │       │           auth.cpython-314.pyc
    │       │           certs.cpython-314.pyc
    │       │           compat.cpython-314.pyc
    │       │           cookies.cpython-314.pyc
    │       │           exceptions.cpython-314.pyc
    │       │           help.cpython-314.pyc
    │       │           hooks.cpython-314.pyc
    │       │           models.cpython-314.pyc
    │       │           packages.cpython-314.pyc
    │       │           sessions.cpython-314.pyc
    │       │           status_codes.cpython-314.pyc
    │       │           structures.cpython-314.pyc
    │       │           utils.cpython-314.pyc
    │       │           _internal_utils.cpython-314.pyc
    │       │           _types.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │           __version__.cpython-314.pyc
    │       │
    │       ├───requests-2.34.2.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   REQUESTED
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │           NOTICE
    │       │
    │       ├───sniffio
    │       │   │   py.typed
    │       │   │   _impl.py
    │       │   │   _version.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───_tests
    │       │   │   │   test_sniffio.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           test_sniffio.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           _impl.cpython-314.pyc
    │       │           _version.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───sniffio-1.3.1.dist-info
    │       │       INSTALLER
    │       │       LICENSE
    │       │       LICENSE.APACHE2
    │       │       LICENSE.MIT
    │       │       METADATA
    │       │       RECORD
    │       │       top_level.txt
    │       │       WHEEL
    │       │
    │       ├───tqdm
    │       │   │   asyncio.py
    │       │   │   auto.py
    │       │   │   autonotebook.py
    │       │   │   cli.py
    │       │   │   completion.sh
    │       │   │   dask.py
    │       │   │   gui.py
    │       │   │   keras.py
    │       │   │   notebook.py
    │       │   │   rich.py
    │       │   │   std.py
    │       │   │   tk.py
    │       │   │   tqdm.1
    │       │   │   utils.py
    │       │   │   version.py
    │       │   │   _main.py
    │       │   │   _monitor.py
    │       │   │   _tqdm.py
    │       │   │   _tqdm_gui.py
    │       │   │   _tqdm_notebook.py
    │       │   │   _tqdm_pandas.py
    │       │   │   _utils.py
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │
    │       │   ├───contrib
    │       │   │   │   bells.py
    │       │   │   │   concurrent.py
    │       │   │   │   discord.py
    │       │   │   │   itertools.py
    │       │   │   │   logging.py
    │       │   │   │   slack.py
    │       │   │   │   telegram.py
    │       │   │   │   utils_worker.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           bells.cpython-314.pyc
    │       │   │           concurrent.cpython-314.pyc
    │       │   │           discord.cpython-314.pyc
    │       │   │           itertools.cpython-314.pyc
    │       │   │           logging.cpython-314.pyc
    │       │   │           slack.cpython-314.pyc
    │       │   │           telegram.cpython-314.pyc
    │       │   │           utils_worker.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           asyncio.cpython-314.pyc
    │       │           auto.cpython-314.pyc
    │       │           autonotebook.cpython-314.pyc
    │       │           cli.cpython-314.pyc
    │       │           dask.cpython-314.pyc
    │       │           gui.cpython-314.pyc
    │       │           keras.cpython-314.pyc
    │       │           notebook.cpython-314.pyc
    │       │           rich.cpython-314.pyc
    │       │           std.cpython-314.pyc
    │       │           tk.cpython-314.pyc
    │       │           utils.cpython-314.pyc
    │       │           version.cpython-314.pyc
    │       │           _main.cpython-314.pyc
    │       │           _monitor.cpython-314.pyc
    │       │           _tqdm.cpython-314.pyc
    │       │           _tqdm_gui.cpython-314.pyc
    │       │           _tqdm_notebook.cpython-314.pyc
    │       │           _tqdm_pandas.cpython-314.pyc
    │       │           _utils.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │
    │       ├───tqdm-4.69.1.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENCE
    │       │
    │       ├───typing_extensions-4.16.0.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───typing_inspection
    │       │   │   introspection.py
    │       │   │   py.typed
    │       │   │   typing_objects.py
    │       │   │   typing_objects.pyi
    │       │   │   __init__.py
    │       │   │
    │       │   └───__pycache__
    │       │           introspection.cpython-314.pyc
    │       │           typing_objects.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───typing_inspection-0.4.2.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───urllib3
    │       │   │   connection.py
    │       │   │   connectionpool.py
    │       │   │   exceptions.py
    │       │   │   fields.py
    │       │   │   filepost.py
    │       │   │   poolmanager.py
    │       │   │   py.typed
    │       │   │   response.py
    │       │   │   _base_connection.py
    │       │   │   _collections.py
    │       │   │   _request_methods.py
    │       │   │   _version.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───contrib
    │       │   │   │   pyopenssl.py
    │       │   │   │   socks.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   ├───emscripten
    │       │   │   │   │   connection.py
    │       │   │   │   │   emscripten_fetch_worker.js
    │       │   │   │   │   fetch.py
    │       │   │   │   │   request.py
    │       │   │   │   │   response.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           connection.cpython-314.pyc
    │       │   │   │           fetch.cpython-314.pyc
    │       │   │   │           request.cpython-314.pyc
    │       │   │   │           response.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           pyopenssl.cpython-314.pyc
    │       │   │           socks.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───http2
    │       │   │   │   connection.py
    │       │   │   │   probe.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           connection.cpython-314.pyc
    │       │   │           probe.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───util
    │       │   │   │   connection.py
    │       │   │   │   proxy.py
    │       │   │   │   request.py
    │       │   │   │   response.py
    │       │   │   │   retry.py
    │       │   │   │   ssltransport.py
    │       │   │   │   ssl_.py
    │       │   │   │   ssl_match_hostname.py
    │       │   │   │   timeout.py
    │       │   │   │   url.py
    │       │   │   │   util.py
    │       │   │   │   wait.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           connection.cpython-314.pyc
    │       │   │           proxy.cpython-314.pyc
    │       │   │           request.cpython-314.pyc
    │       │   │           response.cpython-314.pyc
    │       │   │           retry.cpython-314.pyc
    │       │   │           ssltransport.cpython-314.pyc
    │       │   │           ssl_.cpython-314.pyc
    │       │   │           ssl_match_hostname.cpython-314.pyc
    │       │   │           timeout.cpython-314.pyc
    │       │   │           url.cpython-314.pyc
    │       │   │           util.cpython-314.pyc
    │       │   │           wait.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           connection.cpython-314.pyc
    │       │           connectionpool.cpython-314.pyc
    │       │           exceptions.cpython-314.pyc
    │       │           fields.cpython-314.pyc
    │       │           filepost.cpython-314.pyc
    │       │           poolmanager.cpython-314.pyc
    │       │           response.cpython-314.pyc
    │       │           _base_connection.cpython-314.pyc
    │       │           _collections.cpython-314.pyc
    │       │           _request_methods.cpython-314.pyc
    │       │           _version.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───urllib3-2.7.0.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE.txt
    │       │
    │       └───__pycache__
    │               typing_extensions.cpython-314.pyc
    │
    └───Scripts
            activate
            activate.bat
            activate.fish
            Activate.ps1
            deactivate.bat
            distro.exe
            httpx.exe
            idna.exe
            normalizer.exe
            pip.exe
            pip3.14.exe
            pip3.exe
            python.exe
            pythonw.exe
            tqdm.exe