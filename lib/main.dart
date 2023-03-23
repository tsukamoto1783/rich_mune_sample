import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

void main() async {
  await dotenv.load(fileName: ".env");
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final String? apiGatewayEndpoint = dotenv.env['API_GATEWAY_ENDPOINT'];
  final dio = Dio();

  bool isVisible = false;
  bool isLoading = false;
  Response<dynamic>? callApiResult;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("APIGateway call test"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _buildElevatedButton("Call API ①", true),
            const SizedBox(height: 30),
            _buildElevatedButton("Call API ②", false),
            const SizedBox(height: 30),
            const Text("↓【APIGateway call result】↓"),
            const SizedBox(height: 30),
            _buildResponseDisplay(isVisible, callApiResult),
            isLoading ? const CircularProgressIndicator() : Container(),
          ],
        ),
      ),
    );
  }

  Widget _buildElevatedButton(String buttonText, bool isSwitch) {
    return ElevatedButton(
      child: Text(buttonText),
      onPressed: () async {
        _callApi(isSwitch);
      },
    );
  }

  Widget _buildResponseDisplay(bool isVisible, Response? callApiResult) {
    Widget? displayText;
    if (callApiResult == null) {
      displayText = const Text("API呼び出しに失敗しました");
    }
    return isVisible ? (displayText ?? Text("$callApiResult")) : Container();
  }

  Future<Response?> _callApi(bool isSwitch) async {
    // ボタン押下時の初期化処理
    setState(() {
      isVisible = false;
      callApiResult = null;
      isLoading = true;
    });

    try {
      callApiResult = await dio.get('$apiGatewayEndpoint?is_swithc=$isSwitch');
    } catch (e) {
      print(e);
      throw Exception(e);
    } finally {
      setState(() {
        isVisible = true;
        isLoading = false;
      });
    }
    return callApiResult;
  }
}
