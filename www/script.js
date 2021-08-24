class Slider extends React.Component {
  render() {
    return React.createElement(
      "div",
      null,
      React.createElement("label", null, String(this.props.id) + "."),
      React.createElement("input", {
        type: "range",
        min: -5.5,
        max: 5.5,
        step: 0.1,
        value: this.props.value,
        defaultValue: 0,
        onChange: (event) =>
          this.props.onSlidersChange(+event.target.value, this.props.id - 1),
      }),
      React.createElement("label", null, this.props.value)
    );
  }
}

class Sliders extends React.Component {
  constructor(props) {
    super(props);
  }

  state = {
    values: new Array(512).fill(0),
  };

  _handleChange = (value, index) => {
    const updatedValues = [...this.state.values];
    updatedValues[index] = value;
    this.setState({ values: updatedValues });
  };

  _handleRandom = () => {
    const updatedValues = Array.from({length: 512}, () => Math.floor((Math.random() * 11 - 5.5)*10)/10);
    this.setState({ values: updatedValues });
    this.props.onImageRequest(updatedValues);
  };

  render() {
    return React.createElement(
      "div",
      { className: "d-flex justify-content-center sliders buttons__controls" },
          React.createElement(
            "button",
            {
              className: "btn btn-success btn-lg submit-button",
              type: "button",
              onClick: () => this.props.onImageRequest(this.state.values),
            },
            "Generate"
          ),
          React.createElement(
            "button",
            {
              className: "btn btn-dark btn-lg submit-button",
              type: "button",
              onClick: () => this._handleRandom(),
            },
            "Random"
          ),
        React.createElement(
        "div",
        {className: "slider-div"},
        this.state.values.map((value, index) =>
          React.createElement(Slider, {
            key: index,
            id: index + 1,
            value,
            onSlidersChange: this._handleChange,
            className: "slider"
          })
        )
      )
    );
  }
}

class DragonGenerator extends React.Component {
  constructor(props) {
    super(props);
    this.state = { imagePreviewUrl: "" };
  }

  _handleImageRequest = (parameters) => {
    return new Promise((resolve, reject) => {
      let arrayFormData = new FormData();
      var arrayString = JSON.stringify({ ...parameters });

      arrayFormData.append("array", arrayString);

      var xhr = new XMLHttpRequest();
      var z = this;

      xhr.open("post", "/api/image", true);
      xhr.onload = function () {
        if (this.status == 200) {
          var msg = JSON.parse(this.response);
          z.setState({
            imagePreviewUrl: `data:image/jpeg;base64,${msg.pred.img}`,
          });
          resolve(this.response);
        } else {
          reject(this.statusText);
        }
      };

      xhr.send(arrayFormData);
    });
  };

  render() {
    let { imagePreviewUrl } = this.state;
    let $imagePreview = null;
    if (imagePreviewUrl) {
      $imagePreview = React.createElement("img", {
        className: "mx-auto d-block img-fluid",
        src: imagePreviewUrl,
      });
    } else {
      $imagePreview = React.createElement(
        "div",
        { className: "d-flex justify-content-center font-weight-normal" },
        "Click Generate to generate a dragon!"
      );
    }

    return React.createElement(
      "div",
      { className: "previewComponent" },

      React.createElement("div", {}, $imagePreview),

      React.createElement(
        Sliders,
        { onImageRequest: this._handleImageRequest },
        null
      )
    );
  }
}

ReactDOM.render(
  React.createElement(DragonGenerator, null),
  document.getElementById("mainApp")
);
