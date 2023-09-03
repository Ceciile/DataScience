Using the Apache Beam interactive runner with JupyterLab notebooks lets you iteratively develop pipelines, inspect your pipeline graph, and parse individual PCollections in a read-eval-print-loop (REPL) workflow.

Apache Beam is installed on your notebook instance.


```python
import apache_beam as beam
from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
import apache_beam.runners.interactive.interactive_beam as ib
```

If your notebook uses other Google services:


```python
from apache_beam.options import pipeline_options
from apache_beam.options.pipeline_options import GoogleCloudOptions
import google.auth
```

## Interactivity Options
data capture duration to 60 seconds. If you want to iterate faster, set it to a lower duration, for example ‘10s'.


```python
ib.options.recording_duration = '60s'
```

## Initialize the pipeline using an InteractiveRunner object


```python
# Setting up the Apache Beam pipeline options.
options = pipeline_options.PipelineOptions()

# Set the pipeline mode to stream the data from Pub/Sub.
options.view_as(pipeline_options.StandardOptions).streaming = True

# Sets the project to the default project in your current Google Cloud environment.
# The project will be used for creating a subscription to the Pub/Sub topic.
_, options.view_as(GoogleCloudOptions).project = google.auth.default()

# The Google Cloud PubSub topic for this example.
topic = "projects/pubsub-public-data/topics/shakespeare-kinglear"

p = beam.Pipeline(InteractiveRunner(), options=options)
```

## Reading
an Apache Beam pipeline that creates a subscription to the given Pub/Sub topic and reads from the subscription


```python
words = p | "read" >> beam.io.ReadFromPubSub(topic=topic)
```

    WARNING:apache_beam.options.pipeline_options:Discarding unparseable args: ['-f', '/root/.local/share/jupyter/runtime/kernel-a549cc87-b8f5-48b9-a419-ce14b984922e.json']


**p** counts the words by windows from the source. It creates fixed windowing with each window being 10 seconds in duration.


```python
windowed_words = (words
   | "window" >> beam.WindowInto(beam.window.FixedWindows(10)))
windowed_word_counts = (windowed_words
   | "count" >> beam.combiners.Count.PerElement())
```

## Visualizing the data
`show()` method visualizes the resulting PCollection in the notebook.


```python
ib.show(windowed_word_counts, include_window_info=True)
```



<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<div id="progress_indicator_2beb1fc3001685e83d37caab0ab4086c">
  <div class="spinner-border text-info" role="status"></div>
  <span class="text-info">Processing... show</span>
</div>





<style>
  div.alert {
    white-space: pre-line;
  }
</style>





<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<div class="alert alert-info">Interactive Beam has detected unbounded sources in your pipeline. In order to have a deterministic replay, a segment of data will be recorded from all sources for 60.0 seconds or until a total of 1.0GB have been written to disk.</div>




    <style>
    .p-Widget.jp-OutputPrompt.jp-OutputArea-prompt:empty {
      padding: 0;
      border: 0;
    }
    .p-Widget.jp-RenderedJavaScript.jp-mod-trusted.jp-OutputArea-output:empty {
      padding: 0;
      border: 0;
    }
    </style>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css">
    <table id="table_df_e84a92aa936c722332b734c7ba89db4f" class="display" style="display:block"></table>
    <script>

if (typeof window.interactive_beam_jquery == 'undefined') {
  var jqueryScript = document.createElement('script');
  jqueryScript.src = 'https://code.jquery.com/jquery-3.4.1.slim.min.js';
  jqueryScript.type = 'text/javascript';
  jqueryScript.onload = function() {
    var datatableScript = document.createElement('script');
    datatableScript.src = 'https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js';
    datatableScript.type = 'text/javascript';
    datatableScript.onload = function() {
      window.interactive_beam_jquery = jQuery.noConflict(true);
      window.interactive_beam_jquery(document).ready(function($){

    var dt;
    if ($.fn.dataTable.isDataTable("#table_df_e84a92aa936c722332b734c7ba89db4f")) {
      dt = $("#table_df_e84a92aa936c722332b734c7ba89db4f").dataTable();
    } else if ($("#table_df_e84a92aa936c722332b734c7ba89db4f_wrapper").length == 0) {
      dt = $("#table_df_e84a92aa936c722332b734c7ba89db4f").dataTable({

    bAutoWidth: false,
    columns: [{'title': ''}, {'title': 'windowed_word_counts.0'}, {'title': 'windowed_word_counts.1'}, {'title': 'event_time'}, {'title': 'windows'}, {'title': 'pane_info'}],
    destroy: true,
    responsive: true,
    columnDefs: [
      {
        targets: "_all",
        className: "dt-left"
      },
      {
        "targets": 0,
        "width": "10px",
        "title": ""
      }
    ]
      });
    } else {
      return;
    }
    dt.api()
      .clear()
      .rows.add([{1: "b'a'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 0}, {1: "b'bridegroom'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 1}, {1: "b'laying'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 2}, {1: 'b"autumn\'s"', 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 3}, {1: "b'dust'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 4}, {1: "b'Gentleman'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 5}, {1: "b'Good'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 6}, {1: "b'sir'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 7}, {1: "b'KING'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 8}, {1: "b'LEAR'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 9}, {1: "b'I'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 10}, {1: "b'will'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 11}, {1: "b'die'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 12}, {1: "b'bravely'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 13}, {1: "b'like'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 14}, {1: "b'What'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 15}, {1: "b'be'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 16}, {1: "b'jovial'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 17}, {1: "b'come'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 18}, {1: "b'am'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 19}, {1: "b'king'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 20}, {1: "b'My'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 21}, {1: "b'masters'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 22}, {1: "b'know'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 23}, {1: "b'you'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 24}, {1: "b'that'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 25}, {1: "b'You'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 26}, {1: "b'are'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 27}, {1: "b'royal'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 28}, {1: "b'one'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 29}])
      .draw('full-hold');
      });
    }
    document.head.appendChild(datatableScript);
  };
  document.head.appendChild(jqueryScript);
} else {
  window.interactive_beam_jquery(document).ready(function($){

    var dt;
    if ($.fn.dataTable.isDataTable("#table_df_e84a92aa936c722332b734c7ba89db4f")) {
      dt = $("#table_df_e84a92aa936c722332b734c7ba89db4f").dataTable();
    } else if ($("#table_df_e84a92aa936c722332b734c7ba89db4f_wrapper").length == 0) {
      dt = $("#table_df_e84a92aa936c722332b734c7ba89db4f").dataTable({

    bAutoWidth: false,
    columns: [{'title': ''}, {'title': 'windowed_word_counts.0'}, {'title': 'windowed_word_counts.1'}, {'title': 'event_time'}, {'title': 'windows'}, {'title': 'pane_info'}],
    destroy: true,
    responsive: true,
    columnDefs: [
      {
        targets: "_all",
        className: "dt-left"
      },
      {
        "targets": 0,
        "width": "10px",
        "title": ""
      }
    ]
      });
    } else {
      return;
    }
    dt.api()
      .clear()
      .rows.add([{1: "b'a'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 0}, {1: "b'bridegroom'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 1}, {1: "b'laying'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 2}, {1: 'b"autumn\'s"', 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 3}, {1: "b'dust'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 4}, {1: "b'Gentleman'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 5}, {1: "b'Good'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 6}, {1: "b'sir'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 7}, {1: "b'KING'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 8}, {1: "b'LEAR'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 9}, {1: "b'I'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 10}, {1: "b'will'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 11}, {1: "b'die'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 12}, {1: "b'bravely'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 13}, {1: "b'like'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 14}, {1: "b'What'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 15}, {1: "b'be'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 16}, {1: "b'jovial'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 17}, {1: "b'come'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 18}, {1: "b'am'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 19}, {1: "b'king'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 20}, {1: "b'My'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 21}, {1: "b'masters'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 22}, {1: "b'know'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 23}, {1: "b'you'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 24}, {1: "b'that'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 25}, {1: "b'You'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 26}, {1: "b'are'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 27}, {1: "b'royal'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 28}, {1: "b'one'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 29}])
      .draw('full-hold');
  });
}
    </script>



    <IPython.core.display.Javascript object>




    <style>
    .p-Widget.jp-OutputPrompt.jp-OutputArea-prompt:empty {
      padding: 0;
      border: 0;
    }
    .p-Widget.jp-RenderedJavaScript.jp-mod-trusted.jp-OutputArea-output:empty {
      padding: 0;
      border: 0;
    }
    </style>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css">
    <table id="table_df_e84a92aa936c722332b734c7ba89db4f" class="display" style="display:block"></table>
    <script>

if (typeof window.interactive_beam_jquery == 'undefined') {
  var jqueryScript = document.createElement('script');
  jqueryScript.src = 'https://code.jquery.com/jquery-3.4.1.slim.min.js';
  jqueryScript.type = 'text/javascript';
  jqueryScript.onload = function() {
    var datatableScript = document.createElement('script');
    datatableScript.src = 'https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js';
    datatableScript.type = 'text/javascript';
    datatableScript.onload = function() {
      window.interactive_beam_jquery = jQuery.noConflict(true);
      window.interactive_beam_jquery(document).ready(function($){

    var dt;
    if ($.fn.dataTable.isDataTable("#table_df_e84a92aa936c722332b734c7ba89db4f")) {
      dt = $("#table_df_e84a92aa936c722332b734c7ba89db4f").dataTable();
    } else if ($("#table_df_e84a92aa936c722332b734c7ba89db4f_wrapper").length == 0) {
      dt = $("#table_df_e84a92aa936c722332b734c7ba89db4f").dataTable({

    bAutoWidth: false,
    columns: [{'title': ''}, {'title': 'windowed_word_counts.0'}, {'title': 'windowed_word_counts.1'}, {'title': 'event_time'}, {'title': 'windows'}, {'title': 'pane_info'}],
    destroy: true,
    responsive: true,
    columnDefs: [
      {
        targets: "_all",
        className: "dt-left"
      },
      {
        "targets": 0,
        "width": "10px",
        "title": ""
      }
    ]
      });
    } else {
      return;
    }
    dt.api()
      .clear()
      .rows.add([{1: "b'a'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 0}, {1: "b'bridegroom'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 1}, {1: "b'laying'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 2}, {1: 'b"autumn\'s"', 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 3}, {1: "b'dust'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 4}, {1: "b'Gentleman'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 5}, {1: "b'Good'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 6}, {1: "b'sir'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 7}, {1: "b'KING'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 8}, {1: "b'LEAR'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 9}, {1: "b'I'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 10}, {1: "b'will'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 11}, {1: "b'die'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 12}, {1: "b'bravely'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 13}, {1: "b'like'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 14}, {1: "b'What'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 15}, {1: "b'be'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 16}, {1: "b'jovial'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 17}, {1: "b'come'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 18}, {1: "b'am'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 19}, {1: "b'king'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 20}, {1: "b'My'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 21}, {1: "b'masters'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 22}, {1: "b'know'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 23}, {1: "b'you'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 24}, {1: "b'that'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 25}, {1: "b'You'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 26}, {1: "b'are'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 27}, {1: "b'royal'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 28}, {1: "b'one'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 29}])
      .draw('full-hold');
      });
    }
    document.head.appendChild(datatableScript);
  };
  document.head.appendChild(jqueryScript);
} else {
  window.interactive_beam_jquery(document).ready(function($){

    var dt;
    if ($.fn.dataTable.isDataTable("#table_df_e84a92aa936c722332b734c7ba89db4f")) {
      dt = $("#table_df_e84a92aa936c722332b734c7ba89db4f").dataTable();
    } else if ($("#table_df_e84a92aa936c722332b734c7ba89db4f_wrapper").length == 0) {
      dt = $("#table_df_e84a92aa936c722332b734c7ba89db4f").dataTable({

    bAutoWidth: false,
    columns: [{'title': ''}, {'title': 'windowed_word_counts.0'}, {'title': 'windowed_word_counts.1'}, {'title': 'event_time'}, {'title': 'windows'}, {'title': 'pane_info'}],
    destroy: true,
    responsive: true,
    columnDefs: [
      {
        targets: "_all",
        className: "dt-left"
      },
      {
        "targets": 0,
        "width": "10px",
        "title": ""
      }
    ]
      });
    } else {
      return;
    }
    dt.api()
      .clear()
      .rows.add([{1: "b'a'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 0}, {1: "b'bridegroom'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 1}, {1: "b'laying'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 2}, {1: 'b"autumn\'s"', 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 3}, {1: "b'dust'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 4}, {1: "b'Gentleman'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 5}, {1: "b'Good'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 6}, {1: "b'sir'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 7}, {1: "b'KING'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 8}, {1: "b'LEAR'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 9}, {1: "b'I'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 10}, {1: "b'will'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 11}, {1: "b'die'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 12}, {1: "b'bravely'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 13}, {1: "b'like'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 14}, {1: "b'What'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 15}, {1: "b'be'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 16}, {1: "b'jovial'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 17}, {1: "b'come'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 18}, {1: "b'am'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 19}, {1: "b'king'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 20}, {1: "b'My'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 21}, {1: "b'masters'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 22}, {1: "b'know'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 23}, {1: "b'you'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 24}, {1: "b'that'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 25}, {1: "b'You'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 26}, {1: "b'are'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 27}, {1: "b'royal'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 28}, {1: "b'one'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 29}])
      .draw('full-hold');
  });
}
    </script>






























































































apply multiple filters to your visualizations. The following visualization allows you to filter by label and axis:


```python
ib.show(windowed_word_counts, include_window_info=True, visualize_data=True)
```



<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<div id="progress_indicator_edb357de054486a736971acf55132278">
  <div class="spinner-border text-info" role="status"></div>
  <span class="text-info">Processing... show</span>
</div>





    <style>
    .p-Widget.jp-OutputPrompt.jp-OutputArea-prompt:empty {
      padding: 0;
      border: 0;
    }
    .p-Widget.jp-RenderedJavaScript.jp-mod-trusted.jp-OutputArea-output:empty {
      padding: 0;
      border: 0;
    }
    </style>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css">
    <table id="table_df_b4ec013cb81ee5460ddec3620d3d0103" class="display" style="display:block"></table>
    <script>

if (typeof window.interactive_beam_jquery == 'undefined') {
  var jqueryScript = document.createElement('script');
  jqueryScript.src = 'https://code.jquery.com/jquery-3.4.1.slim.min.js';
  jqueryScript.type = 'text/javascript';
  jqueryScript.onload = function() {
    var datatableScript = document.createElement('script');
    datatableScript.src = 'https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js';
    datatableScript.type = 'text/javascript';
    datatableScript.onload = function() {
      window.interactive_beam_jquery = jQuery.noConflict(true);
      window.interactive_beam_jquery(document).ready(function($){

    var dt;
    if ($.fn.dataTable.isDataTable("#table_df_b4ec013cb81ee5460ddec3620d3d0103")) {
      dt = $("#table_df_b4ec013cb81ee5460ddec3620d3d0103").dataTable();
    } else if ($("#table_df_b4ec013cb81ee5460ddec3620d3d0103_wrapper").length == 0) {
      dt = $("#table_df_b4ec013cb81ee5460ddec3620d3d0103").dataTable({

    bAutoWidth: false,
    columns: [{'title': ''}, {'title': 'windowed_word_counts.0'}, {'title': 'windowed_word_counts.1'}, {'title': 'event_time'}, {'title': 'windows'}, {'title': 'pane_info'}],
    destroy: true,
    responsive: true,
    columnDefs: [
      {
        targets: "_all",
        className: "dt-left"
      },
      {
        "targets": 0,
        "width": "10px",
        "title": ""
      }
    ]
      });
    } else {
      return;
    }
    dt.api()
      .clear()
      .rows.add([{1: "b'a'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 0}, {1: "b'bridegroom'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 1}, {1: "b'laying'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 2}, {1: 'b"autumn\'s"', 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 3}, {1: "b'dust'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 4}, {1: "b'Gentleman'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 5}, {1: "b'Good'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 6}, {1: "b'sir'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 7}, {1: "b'KING'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 8}, {1: "b'LEAR'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 9}, {1: "b'I'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 10}, {1: "b'will'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 11}, {1: "b'die'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 12}, {1: "b'bravely'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 13}, {1: "b'like'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 14}, {1: "b'What'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 15}, {1: "b'be'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 16}, {1: "b'jovial'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 17}, {1: "b'come'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 18}, {1: "b'am'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 19}, {1: "b'king'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 20}, {1: "b'My'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 21}, {1: "b'masters'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 22}, {1: "b'know'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 23}, {1: "b'you'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 24}, {1: "b'that'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 25}, {1: "b'You'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 26}, {1: "b'are'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 27}, {1: "b'royal'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 28}, {1: "b'one'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 29}])
      .draw('full-hold');
      });
    }
    document.head.appendChild(datatableScript);
  };
  document.head.appendChild(jqueryScript);
} else {
  window.interactive_beam_jquery(document).ready(function($){

    var dt;
    if ($.fn.dataTable.isDataTable("#table_df_b4ec013cb81ee5460ddec3620d3d0103")) {
      dt = $("#table_df_b4ec013cb81ee5460ddec3620d3d0103").dataTable();
    } else if ($("#table_df_b4ec013cb81ee5460ddec3620d3d0103_wrapper").length == 0) {
      dt = $("#table_df_b4ec013cb81ee5460ddec3620d3d0103").dataTable({

    bAutoWidth: false,
    columns: [{'title': ''}, {'title': 'windowed_word_counts.0'}, {'title': 'windowed_word_counts.1'}, {'title': 'event_time'}, {'title': 'windows'}, {'title': 'pane_info'}],
    destroy: true,
    responsive: true,
    columnDefs: [
      {
        targets: "_all",
        className: "dt-left"
      },
      {
        "targets": 0,
        "width": "10px",
        "title": ""
      }
    ]
      });
    } else {
      return;
    }
    dt.api()
      .clear()
      .rows.add([{1: "b'a'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 0}, {1: "b'bridegroom'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 1}, {1: "b'laying'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 2}, {1: 'b"autumn\'s"', 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 3}, {1: "b'dust'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 4}, {1: "b'Gentleman'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 5}, {1: "b'Good'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 6}, {1: "b'sir'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 7}, {1: "b'KING'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 8}, {1: "b'LEAR'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 9}, {1: "b'I'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 10}, {1: "b'will'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 11}, {1: "b'die'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 12}, {1: "b'bravely'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 13}, {1: "b'like'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 14}, {1: "b'What'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 15}, {1: "b'be'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 16}, {1: "b'jovial'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 17}, {1: "b'come'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 18}, {1: "b'am'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 19}, {1: "b'king'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 20}, {1: "b'My'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 21}, {1: "b'masters'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 22}, {1: "b'know'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 23}, {1: "b'you'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 24}, {1: "b'that'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 25}, {1: "b'You'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 26}, {1: "b'are'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 27}, {1: "b'royal'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 28}, {1: "b'one'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 29}])
      .draw('full-hold');
  });
}
    </script>




<style>
.p-Widget.jp-OutputPrompt.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}
.p-Widget.jp-RenderedJavaScript.jp-mod-trusted.jp-OutputArea-output:empty {
  padding: 0;
  border: 0;
}
</style>
<iframe id=facets_dive_b4ec013cb81ee5460ddec3620d3d0103 style="border:none" width="100%" height="600px"
  srcdoc='
    <script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.3.3/webcomponents-lite.js"></script>
    <link rel="import" href="https://raw.githubusercontent.com/PAIR-code/facets/1.0.0/facets-dist/facets-jupyter.html">
    <facets-dive sprite-image-width="64" sprite-image-height="64" id="facets_dive_b4ec013cb81ee5460ddec3620d3d0103" height="600"></facets-dive>
    <script>
      document.getElementById("facets_dive_b4ec013cb81ee5460ddec3620d3d0103").data = [];
    </script>
  '>
</iframe>




<style>
.p-Widget.jp-OutputPrompt.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}
.p-Widget.jp-RenderedJavaScript.jp-mod-trusted.jp-OutputArea-output:empty {
  padding: 0;
  border: 0;
}
</style>
<iframe id=facets_overview_b4ec013cb81ee5460ddec3620d3d0103 style="border:none" width="100%" height="600px"
  srcdoc='
    <script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.3.3/webcomponents-lite.js"></script>
    <link rel="import" href="https://raw.githubusercontent.com/PAIR-code/facets/1.0.0/facets-dist/facets-jupyter.html">
    <facets-overview id="facets_overview_b4ec013cb81ee5460ddec3620d3d0103"></facets-overview>
    <script>
      document.getElementById("facets_overview_b4ec013cb81ee5460ddec3620d3d0103").protoInput = "Cj4KBGRhdGEaEgoKZXZlbnRfdGltZRACIgIKABoPCgd3aW5kb3dzEAIiAgoAGhEKCXBhbmVfaW5mbxACIgIKAA==";
    </script>
  '>
</iframe>



    <IPython.core.display.Javascript object>




    <style>
    .p-Widget.jp-OutputPrompt.jp-OutputArea-prompt:empty {
      padding: 0;
      border: 0;
    }
    .p-Widget.jp-RenderedJavaScript.jp-mod-trusted.jp-OutputArea-output:empty {
      padding: 0;
      border: 0;
    }
    </style>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css">
    <table id="table_df_b4ec013cb81ee5460ddec3620d3d0103" class="display" style="display:block"></table>
    <script>

if (typeof window.interactive_beam_jquery == 'undefined') {
  var jqueryScript = document.createElement('script');
  jqueryScript.src = 'https://code.jquery.com/jquery-3.4.1.slim.min.js';
  jqueryScript.type = 'text/javascript';
  jqueryScript.onload = function() {
    var datatableScript = document.createElement('script');
    datatableScript.src = 'https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js';
    datatableScript.type = 'text/javascript';
    datatableScript.onload = function() {
      window.interactive_beam_jquery = jQuery.noConflict(true);
      window.interactive_beam_jquery(document).ready(function($){

    var dt;
    if ($.fn.dataTable.isDataTable("#table_df_b4ec013cb81ee5460ddec3620d3d0103")) {
      dt = $("#table_df_b4ec013cb81ee5460ddec3620d3d0103").dataTable();
    } else if ($("#table_df_b4ec013cb81ee5460ddec3620d3d0103_wrapper").length == 0) {
      dt = $("#table_df_b4ec013cb81ee5460ddec3620d3d0103").dataTable({

    bAutoWidth: false,
    columns: [{'title': ''}, {'title': 'windowed_word_counts.0'}, {'title': 'windowed_word_counts.1'}, {'title': 'event_time'}, {'title': 'windows'}, {'title': 'pane_info'}],
    destroy: true,
    responsive: true,
    columnDefs: [
      {
        targets: "_all",
        className: "dt-left"
      },
      {
        "targets": 0,
        "width": "10px",
        "title": ""
      }
    ]
      });
    } else {
      return;
    }
    dt.api()
      .clear()
      .rows.add([{1: "b'a'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 0}, {1: "b'bridegroom'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 1}, {1: "b'laying'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 2}, {1: 'b"autumn\'s"', 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 3}, {1: "b'dust'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 4}, {1: "b'Gentleman'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 5}, {1: "b'Good'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 6}, {1: "b'sir'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 7}, {1: "b'KING'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 8}, {1: "b'LEAR'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 9}, {1: "b'I'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 10}, {1: "b'will'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 11}, {1: "b'die'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 12}, {1: "b'bravely'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 13}, {1: "b'like'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 14}, {1: "b'What'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 15}, {1: "b'be'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 16}, {1: "b'jovial'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 17}, {1: "b'come'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 18}, {1: "b'am'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 19}, {1: "b'king'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 20}, {1: "b'My'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 21}, {1: "b'masters'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 22}, {1: "b'know'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 23}, {1: "b'you'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 24}, {1: "b'that'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 25}, {1: "b'You'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 26}, {1: "b'are'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 27}, {1: "b'royal'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 28}, {1: "b'one'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 29}])
      .draw('full-hold');
      });
    }
    document.head.appendChild(datatableScript);
  };
  document.head.appendChild(jqueryScript);
} else {
  window.interactive_beam_jquery(document).ready(function($){

    var dt;
    if ($.fn.dataTable.isDataTable("#table_df_b4ec013cb81ee5460ddec3620d3d0103")) {
      dt = $("#table_df_b4ec013cb81ee5460ddec3620d3d0103").dataTable();
    } else if ($("#table_df_b4ec013cb81ee5460ddec3620d3d0103_wrapper").length == 0) {
      dt = $("#table_df_b4ec013cb81ee5460ddec3620d3d0103").dataTable({

    bAutoWidth: false,
    columns: [{'title': ''}, {'title': 'windowed_word_counts.0'}, {'title': 'windowed_word_counts.1'}, {'title': 'event_time'}, {'title': 'windows'}, {'title': 'pane_info'}],
    destroy: true,
    responsive: true,
    columnDefs: [
      {
        targets: "_all",
        className: "dt-left"
      },
      {
        "targets": 0,
        "width": "10px",
        "title": ""
      }
    ]
      });
    } else {
      return;
    }
    dt.api()
      .clear()
      .rows.add([{1: "b'a'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 0}, {1: "b'bridegroom'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 1}, {1: "b'laying'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 2}, {1: 'b"autumn\'s"', 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 3}, {1: "b'dust'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 4}, {1: "b'Gentleman'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 5}, {1: "b'Good'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 6}, {1: "b'sir'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 7}, {1: "b'KING'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 8}, {1: "b'LEAR'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 9}, {1: "b'I'", 2: '3', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 10}, {1: "b'will'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 11}, {1: "b'die'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 12}, {1: "b'bravely'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 13}, {1: "b'like'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 14}, {1: "b'What'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 15}, {1: "b'be'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 16}, {1: "b'jovial'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 17}, {1: "b'come'", 2: '2', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 18}, {1: "b'am'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 19}, {1: "b'king'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 20}, {1: "b'My'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 21}, {1: "b'masters'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 22}, {1: "b'know'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 23}, {1: "b'you'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 24}, {1: "b'that'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 25}, {1: "b'You'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 26}, {1: "b'are'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 27}, {1: "b'royal'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 28}, {1: "b'one'", 2: '1', 3: '2023-09-03 14:19:49.999999+0000', 4: '2023-09-03 14:19:40.000000+0000 (10s)', 5: 'Pane 0', 0: 29}])
      .draw('full-hold');
  });
}
    </script>


















































### output in a Pandas DataFrame
first converts the words to lowercase and then computes the frequency of each word.


```python
windowed_lower_word_counts = (windowed_words
   | "to lower case" >> beam.Map(lambda word: word.lower())
   | "count lowered" >> beam.combiners.Count.PerElement())
ib.collect(windowed_lower_word_counts, include_window_info=True)
```



<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<div id="progress_indicator_37b31a06917e41be6d065675c8f5704d">
  <div class="spinner-border text-info" role="status"></div>
  <span class="text-info">Processing... collect</span>
</div>








<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>event_time</th>
      <th>windows</th>
      <th>pane_info</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b'a'</td>
      <td>3</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b'bridegroom'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b'laying'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b"autumn's"</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b'dust'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b'gentleman'</td>
      <td>2</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>b'good'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>b'sir'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>b'king'</td>
      <td>2</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>b'lear'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>b'i'</td>
      <td>3</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>b'will'</td>
      <td>2</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>b'die'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>b'bravely'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>b'like'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>b'what'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>b'be'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>b'jovial'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>b'come'</td>
      <td>2</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>b'am'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>b'my'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>b'masters'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>b'know'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>b'you'</td>
      <td>2</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>b'that'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>b'are'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>b'royal'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>b'one'</td>
      <td>1</td>
      <td>1693750789999999</td>
      <td>[[1693750780.0, 1693750790.0)]</td>
      <td>PaneInfo(first: True, last: False, timing: ON_...</td>
    </tr>
  </tbody>
</table>
</div>


