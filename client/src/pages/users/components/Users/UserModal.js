import React, { Component } from 'react';
import { Modal, Form, Input } from 'antd';

const FormItem = Form.Item;

class UserEditModal extends Component {
  constructor(props) {
    super(props);
    console.log("UserEditModal.constructor",props)
    this.state = { visible: false, };
  }

  showModelHandler = e => {
    if (e) e.stopPropagation();
    this.setState({ visible: true, });
  };

  hideModelHandler = () => {
    this.setState({ visible: false, });
  };

  okHandler = () => {
    const { onOk } = this.props;
    this.props.form.validateFields((err, values) => {
      if (!err) {
        onOk(values);
        this.hideModelHandler();
      }
    });
  };

  render() {
    const { children } = this.props;
    const { getFieldDecorator } = this.props.form;
    const { name, email, website } = this.props.record;
    const formItemLayout = { labelCol: { span: 6 }, wrapperCol: { span: 14 }, };

    return (
      <span>
        <span onClick={this.showModelHandler}>{children}</span>
        <Modal title="Edit User" visible={this.state.visible} onOk={this.okHandler} onCancel={this.hideModelHandler} >
          <Form layout="horizontal" onSubmit={this.okHandler}>
            <FormItem {...formItemLayout} label="姓名">
              {getFieldDecorator('name', { initialValue: name, })(<Input />)}
            </FormItem>
            <FormItem {...formItemLayout} label="邮件地址">
              {getFieldDecorator('email', { initialValue: email, })(<Input />)}
            </FormItem>
            <FormItem {...formItemLayout} label="网址">
              {getFieldDecorator('website', { initialValue: website, })(<Input />)}
            </FormItem>
          </Form>
        </Modal>
      </span>
    );
  }
}

export default Form.create()(UserEditModal);
